from django.shortcuts import get_object_or_404, render

# Create your views here.
#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Lemma
from django import template

register = template.Library()

def get_children(level, root):
    children = level[root['wordorder']] if root['wordorder'] in level else [] 
    for child in children:
        child['children'] = get_children(level, child)
        child['parent'] = root['name']
    return children

def treemaker(lemma_list):
    tree = {}
    # sorting into dependency groups
    dep_dict = {}
    for obj in lemma_list:
        item = {'name': obj.lemma, 'wordorder': obj.word_order}
        dep_dict[obj.dependency] = dep_dict[obj.dependency] + [item] if obj.dependency in dep_dict else [item]
    print(dep_dict[0][0]['name'])
    tree['name'] = dep_dict[0][0]['name']
    tree['children'] = get_children(dep_dict, dep_dict[0][0])
    tree['parent'] = 'null'
    return tree

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Lemma
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        query_meta = self.request.GET.get('q_meta')
        object_list = Lemma.objects.filter(
        		Q(wordform__trigram_similar=query) | Q(lemma__trigram_similar=query) | Q(key__text_index__exact=query_meta)
        		#Q(key__text_index__exact=query_meta)
           #Q(wordform__icontains='ana') | Q(lemma__icontains='umma')
           )
        #if q_meta not None:
       # 	meta_object_list = 
        all_keys = set([el.group_key for el in object_list])
        #all_lemmas = [el.group_key.lemmas for el in object_list]
        # clauses
        all_lemmas = [Lemma.objects.filter(
           Q(group_key__exact=key) 
        ) for key in all_keys]
        trees = []
        # going for each clause
        for elList in all_lemmas:
        	#for el in elList:
        		#if el.lemma in [r.lemma for r in object_list]:
        	trees.append({
        		'obj': elList[0].group_key,  #return clause
        		'tree': treemaker(elList),
        		'lemmas': elList,
        		'meta': elList[0].key, #return meta 
        		})       
        #trees = [{'obj': el.lemma if el.lemma in [r.lemma for r in object_list] else None, 'tree': treemaker(el)} for elList in all_lemmas]
        #select * from lemma where lemma.group_key = query.group_key

        view_object = {"query": {'wordform': query, 'index': query_meta}, "trees": trees}
        return view_object

class DetailView(TemplateView):
    template_name = "clauseDetail.html"