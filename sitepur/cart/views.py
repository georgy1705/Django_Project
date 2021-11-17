from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views import View
from catalog.mixins import CartMixin
from django.http import HttpResponseRedirect
from catalog.models import Articles, Cart, Customer, CartProduct
from catalog.utils import recalc_cart
from .forms import CartAddProductForm


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'cart': self.cart,
        }
        return render(request, 'cart/detail.html', context)


class AddToCartView(CartMixin, View):
    def get(self, request, product_id, *args, **kwargs):
        product = Articles.objects.get(id=product_id)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        return HttpResponseRedirect('/cart/')


class DeleteFromCartView(CartMixin, View):
    def get(self, request, product_id, *args, **kwargs):
        product = Articles.objects.get(id=product_id)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, product=product
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')


class ChangeQtyView(CartMixin, View):

    def post(self, request, product_id, *args, **kwargs):
        product = Articles.objects.get(id=product_id)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, product=product
        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
        return HttpResponseRedirect('/cart/')



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Articles, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

