from django.db import models
from filer.fields.image import FilerImageField

class Articles(models.Model):
    img = models.ImageField('Фотография', upload_to='sneakers_logos')
    slug = models.SlugField()
    title = models.CharField('Название', max_length=50)
    price = models.CharField('Цена', max_length=20)
    description = models.TextField('Описание вещи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все кроссовки'
        verbose_name_plural = 'Кроссовки'

class ArticlesImage(models.Model):
    post = models.ForeignKey(Articles, default=None, on_delete=models.CASCADE)
    img_detail = models.ImageField('Фотографии модели', upload_to='sneakers_img')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Фотография модели'
        verbose_name_plural = 'Фотографии модели кроссовок'


