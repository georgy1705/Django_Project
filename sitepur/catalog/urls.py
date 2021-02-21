from django.urls import path
from . import views

urlpatterns = [
    path('sneakers', views.catalog_home, name='catalog_home'),
    path('sneakers/<slug:slug>', views.ShoesDetailView.as_view(), name='shoes-detail')
]