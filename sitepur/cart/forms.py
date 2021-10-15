from django import forms
from catalog.models import Articles


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label = 'Количество',
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput)

