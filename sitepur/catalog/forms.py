from catalog.models import Reviews
from django.forms import ModelForm, Textarea, ImageField
from django.utils.safestring import mark_safe


class ReviewForm(ModelForm):
    img_detail = ImageField()
    class Meta:
        model = Reviews
        fields = ['text', 'img_detail']
        widgets = {
            "text": Textarea(attrs={
            'rows': 5,
            'class': 'form-control',
            'placeholder': 'Текст комментария'
        }),
        }