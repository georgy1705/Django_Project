from django.shortcuts import render, get_object_or_404
from .models import Articles, ArticlesImage, Gender, Subcategory, Brand
from django.views.generic import DetailView
from django.db.models import Q


def catalog_home(request):
    catalog = Articles.objects.all()
    gen = Gender.objects.all()
    brand = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request, 'catalog/catalog_home.html', {'catalog': catalog, 'genders': gen, 'subcategory': subcategory, 'brand': brand})

class ShoesDetailView(DetailView):
    model = Articles
    template_name = 'catalog/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShoesDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['articleimg'] = ArticlesImage.objects.filter(post=self.object)
        return context


def FilterCatalogView(request):
    catalog = Articles.objects.all()
    if "gender" in request.GET:
        catalog= catalog.filter(gender__name__in=request.GET.getlist("gender"))
    if "subcategory" in request.GET:
        catalog = catalog.filter(subcategory__name__in=request.GET.getlist("subcategory"))
    if "brand" in request.GET:
        catalog = catalog.filter(brand__name__in=request.GET.getlist("brand"))

    gen = Gender.objects.all()
    brand = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request, 'catalog/catalog_home.html',
                  {'catalog': catalog, 'genders': gen, 'subcategory': subcategory, 'brand': brand})


def Search(request):
    catalog = Articles.objects.filter(title__icontains=request.GET.get("search"))
    gen = Gender.objects.all()
    brand = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request, 'catalog/catalog_home.html',
                  {'catalog': catalog, 'genders': gen, 'subcategory': subcategory, 'brand': brand})




