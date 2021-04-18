from django.urls import path

#from . import views

#urlpatterns = [
#    path('', views.index, name='index')
#]
from .views import HomePageView, SearchResultsView, DetailView

urlpatterns = [
    path('clause/', DetailView.as_view(), name='detail_view'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]