from django.shortcuts import render
from catalog.models import Customer, Cart


def index(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)

    if request.user.is_authenticated:
        return render(request, 'main/index.html', {'cart': cart})
    else:
        return render(request, 'main/index.html')

def about(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)

    if request.user.is_authenticated:
        return render(request, 'main/about.html', {'cart': cart})
    else:
        return render(request, 'main/about.html')