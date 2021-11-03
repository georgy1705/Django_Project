from django.shortcuts import render, get_object_or_404
from .models import Articles, ArticlesImage, Gender, Subcategory, Brand, Category, Size
from django.views.generic import DetailView
from django.db.models import Q
from cart.forms import CartAddProductForm


def catalog_home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    catalog = Articles.objects.filter(available=True)
    subcategory = Subcategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        catalog = Articles.objects.filter(category=category, available=True)
        subcategory = Subcategory.objects.filter(articles__category=category).distinct()
    gen = Gender.objects.all()
    brand = Brand.objects.all()
    return render(request, 'catalog/catalog_home.html', {'catalog': catalog, 'category': category, 'categories': categories,
                                                         'genders': gen, 'subcategory': subcategory,
                                                         'brand': brand})

class ShoesDetailView(DetailView):
    model = Articles
    template_name = 'catalog/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShoesDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['articleimg'] = ArticlesImage.objects.filter(post=self.object)
        context['size'] = Size.objects.filter(post=self.object)
        context['cart_product_form'] = CartAddProductForm()
        return context


def FilterCatalogView(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    catalog = Articles.objects.filter(available=True)
    subcategory = Subcategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        catalog = Articles.objects.filter(category=category, available=True)
        subcategory = Subcategory.objects.filter(articles__category=category).distinct()
    if "gender" in request.GET:
        catalog= catalog.filter(gender__name__in=request.GET.getlist("gender"), available=True)
    if "subcategory" in request.GET:
        catalog = catalog.filter(subcategory__name__in=request.GET.getlist("subcategory"), available=True)
    if "brand" in request.GET:
        catalog = catalog.filter(brand__name__in=request.GET.getlist("brand"), available=True)

    gen = Gender.objects.all()
    brand = Brand.objects.all()
    return render(request, 'catalog/catalog_home.html',
                  {'catalog': catalog, 'category': category, 'categories': categories,
                   'genders': gen, 'subcategory': subcategory, 'brand': brand})


def Search(request):
    catalog = Articles.objects.filter(title__icontains=request.GET.get("search"), available=True)
    gen = Gender.objects.all()
    brand = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request, 'catalog/catalog_home.html',
                  {'catalog': catalog, 'genders': gen, 'subcategory': subcategory, 'brand': brand})


