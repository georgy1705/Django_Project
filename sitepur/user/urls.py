from django.urls import path
from . import views
from .views import MakeOrderView, CheckoutView

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('make-order', MakeOrderView.as_view(), name='make-order')
]