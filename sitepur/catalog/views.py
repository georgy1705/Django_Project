from django.shortcuts import render
from .models import Articles

def catalog_home(request):
    catalog = Articles.objects.all()
    return render(request, 'catalog/catalog_home.html', {'catalog': catalog})

