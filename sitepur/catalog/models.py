from django.db import models

class Articles(models.Model):
    img = models.ImageField(upload_to='sneakers_logos')
    title = models.CharField('Название', max_length=50)
    price = models.CharField('Цена', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все кроссовки'
        verbose_name_plural = 'Кроссовки'

