from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from user.models import User, Order
from datetime import date, timedelta


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('email', 'phone', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class OrderForm(forms.ModelForm):
    phone = PhoneNumberField(label='Телефон',  error_messages={'unique': 'Please enter your phone'}, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий к заказу', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    order_date = forms.DateField(label='Дата получения заказа', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today()+timedelta(days=3), 'readonly':'readonly'}))
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


