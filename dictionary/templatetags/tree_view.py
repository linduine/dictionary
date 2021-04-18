from django import template

register = template.Library()
@register.inclusion_tag('detail_view.html', takes_context=True)
def tree_view(context):
	return {
	    'lemma': context['lemma_el']['obj'].lemma,
        'tree': context['lemma_el']['tree'],
    }