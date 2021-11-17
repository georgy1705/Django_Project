from django.urls import path
from . import views
from .views import CartView, AddToCartView, DeleteFromCartView, ChangeQtyView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/',
         AddToCartView.as_view(),
         name='cart_add'),
    path('remove/<int:product_id>/',
         views.DeleteFromCartView.as_view(),
         name='cart_remove'),
    path('change-qty/<int:product_id>/',
         views.ChangeQtyView.as_view(),
         name='cart_change'),
]