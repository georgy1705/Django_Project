from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogHome.as_view(), name='catalog_home'),
    path('sizes/', views.Sizes, name='sizes'),
    path("filter/", views.FilterCatalogView, name="filter1"),
    path("<slug:category_slug>/filter/", views.FilterCatalogView, name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path('<slug:category_slug>/', views.CatalogHome.as_view(), name='catalog_home_by_category'),
    path('<slug:category_slug>/<slug:slug>', views.ShoesDetailView.as_view(), name='shoes-detail')
]