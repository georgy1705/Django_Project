from django.urls import path
from . import views

urlpatterns = [
    path('sneakers', views.catalog_home, name='catalog_home'),
]