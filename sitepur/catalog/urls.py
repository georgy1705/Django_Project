from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path("filter/", views.FilterCatalogView, name="filter"),
    path("search/", views.Search, name="search"),
    path('<slug:category_slug>/', views.catalog_home, name='catalog_home_by_category'),
    path('<slug:category_slug>/<slug:slug>', views.ShoesDetailView.as_view(), name='shoes-detail')
]