from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, OrderForm
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic import View
from .models import User, Customer
from catalog.mixins import CartMixin



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'user/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли')
            return redirect('home')
    else:
        form = UserLoginForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'user/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')



class CheckoutView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'form': form
        }
        return render(request, 'user/checkout.html', context)



class MakeOrderView(CartMixin, View):


    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, 'Спасибо за заказ! Менеджер с Вами свяжется.')
            return HttpResponseRedirect('/catalog/')
        else:
            messages.error(request, 'Неправильно введены данные')
            return render(request, 'user/checkout.html', context={'form': form, 'cart': self.cart,})


# else:
        #     messages.error(request, 'Ошибка регистрации')


