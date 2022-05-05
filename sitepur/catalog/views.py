from django.shortcuts import render, get_object_or_404
from .models import Articles, ArticlesImage, Gender, Subcategory, Brand, Category, Size, Customer, Cart
from .mixins import CartMixin
from django.views.generic import DetailView, View
from django.db.models import Q
from cart.forms import CartAddProductForm
from .forms import ReviewForm
from django.views.generic.edit import FormMixin
from django.http import Http404



class CatalogHome(CartMixin, View):

    def get(self, request, category_slug=None, *args, **kwargs):
        category = None
        categories = Category.objects.all()
        catalog = Articles.objects.filter(available=True)
        subcategory = Subcategory.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            catalog = Articles.objects.filter(category=category, available=True)
            subcategory = Subcategory.objects.filter(articles__category=category).distinct()
        print(category_slug)
        gen = Gender.objects.all()
        brand = Brand.objects.all()
        context = {'catalog': catalog, 'category': category, 'categories': categories,
                                                         'genders': gen, 'subcategory': subcategory,
                                                         'brand': brand, 'cart': self.cart}
        return render(request, 'catalog/catalog_home.html', context)

class ShoesDetailView(CartMixin, FormMixin, DetailView):
    model = Articles
    template_name = 'catalog/details_view.html'
    context_object_name = 'article'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShoesDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['articleimg'] = ArticlesImage.objects.filter(post=self.object)
        context['size'] = Size.objects.filter(post=self.object)
        context['cart_product_form'] = CartAddProductForm()
        context['cart'] = self.cart
        context['form'] = self.get_form()
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.img = form.instance
        self.object.save()
        return super(ShoesDetailView, self).form_valid(form)

    def form_invalid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.img = form.instance
        self.object.save()
        return super(ShoesDetailView, self).form_invalid(form)




def FilterCatalogView(request, category_slug=None):
    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user)
        cart = Cart.objects.filter(owner=customer)
    category = None
    categories = Category.objects.all()
    catalog = Articles.objects.filter(available=True)
    subcategory = Subcategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        catalog = Articles.objects.filter(category=category, available=True)
        subcategory = Subcategory.objects.filter(articles__category=category).distinct()
    if "sort" in request.GET:
        if request.GET.getlist("sort") == ['max']:
            catalog = catalog.order_by('-price')
        elif request.GET.getlist("sort") == ['min']:
            catalog = catalog.order_by('price')
        elif request.GET.getlist("sort") == ['new']:
            catalog = catalog.order_by('title')
        elif request.GET.getlist("sort") == ['latest']:
            catalog = catalog.order_by('-title')
        else:
            pass
    if "gender" in request.GET:
        catalog = catalog.filter(gender__name__in=request.GET.getlist("gender"), available=True)
    if "subcategory" in request.GET:
        catalog = catalog.filter(subcategory__name__in=request.GET.getlist("subcategory"), available=True)
    if "brand" in request.GET:
        catalog = catalog.filter(brand__name__in=request.GET.getlist("brand"), available=True)

    gen = Gender.objects.all()
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog/catalog_home.html',
                  {'catalog': catalog, 'category': category, 'categories': categories,
                   'genders': gen, 'subcategory': subcategory, 'brand': brand, 'cart': cart})
    else:
        return render(request, 'catalog/catalog_home.html',
                      {'catalog': catalog, 'category': category, 'categories': categories,
                       'genders': gen, 'subcategory': subcategory, 'brand': brand})


class Search(CartMixin, View):
    def get(self, request, *args, **kwargs):
        catalog = Articles.objects.filter(title__icontains=request.GET.get("search"), available=True)
        gen = Gender.objects.all()
        brand = Brand.objects.all()
        subcategory = Subcategory.objects.all()
        return render(request, 'catalog/catalog_home.html',
                      {'catalog': catalog, 'genders': gen, 'subcategory': subcategory, 'brand': brand, 'cart': self.cart})


def Sizes(request):
    return render(request, 'catalog/sizes.html')


