from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, OrderForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import User
from cart.cart import Cart

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

def checkout(request):
    check = Cart(request)
    form = OrderForm(request.POST or None)
    return render(request, 'user/checkout.html', {'check': check, "form": form})


# class ProfileView(CartMixin, View):
#
#     def get(self, request, *args, **kwargs):
#         user = User.objects.get(user=request.user)
#         # orders = Order.objects.filter(user=user).order_by('-created_at')
#         # categories = Category.objects.all()
#
#         return render(
#             request,
#             'profile.html',
#             {'cart': self.cart}
#         )

