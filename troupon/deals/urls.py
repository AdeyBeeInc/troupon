
from django.conf.urls import url, include
from .views import DealSearchView, DealSearchCityView, DealView, DealsView, CategoryView, DealCategoryView, DealSlugView


urlpatterns = [
    url(r'^search/', include('haystack.urls')),
    url(r'^search/entry/$', DealSearchView.as_view(), name = 'dealsearch'),
    url(r'^search/cities/$', DealSearchCityView.as_view(), name ='dealsearchcity'),
    # /deals/
    url(r'^$', DealsView.as_view(), name='deals'),
    # /deals/:id
    url(r'^(?P<deal_id>[0-9]+)/$', DealView.as_view(), name='deal'),
    # /deals/categories/
    url(r'^categories/$',
        CategoryView.as_view(),
        name='deal-categories'),
    # /deals/:slug
    url(r'^(?P<deal_slug>[\w-]+)/$',
        DealSlugView.as_view(),
        name='deal-with-slug'),
    # /deals/category/:slug
    url(r'^category/(?P<category_slug>[\w-]+)/$',
        DealCategoryView.as_view(),
        name='deal-category-with-slug'),
]
