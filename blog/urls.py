from django.conf.urls import url
from .views import (index, detail, archives, categories, IndexView, ArchivesView, CategoriesView, PostDetailView
                    , TagsView, search, KnowledgeView, PhotosView, ShoesView, NewsView)

app_name = 'blog'

urlpatterns = [
    #url(r'^index/$', index, name='index'),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^knowledge/$', KnowledgeView.as_view(), name='knowledge'),
    url(r'^photos/$', PhotosView.as_view(), name='photos'),
    url(r'^shoes/$', ShoesView.as_view(), name='shoes'),
    url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[1-9]|1[0-2])/$', ArchivesView.as_view(), name='archives'),
    url(r'^categories/(?P<pk>\d+)/$', CategoriesView.as_view(), name='categories'),
    url(r'^tags/(?P<pk>\d+)/$', TagsView.as_view(), name='tags'),
    # url(r'^search/$', search, name='search'),
]