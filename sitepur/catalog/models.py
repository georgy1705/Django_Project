from django.db import models
from filer.fields.image import FilerImageField
from slugify import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Gender(models.Model):
    name = models.CharField("Пол", max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

class Subcategory(models.Model):
    name = models.CharField("Подкатегория", max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Brand(models.Model):
    name = models.CharField("Бренд", max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Articles(models.Model):
    img = models.ImageField(upload_to='sneakers_logos')
    img_thumbnail = ImageSpecField(source='img',
                                      processors=[ResizeToFill(1000, 950)],
                                      format='JPEG',
                                      options={'quality': 60})

    title = models.CharField('Название', max_length=50)
    slug = models.SlugField(unique=True)
    price = models.CharField('Цена', max_length=20)
    description = models.TextField('Описание вещи')
    gender = models.ForeignKey(Gender, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, verbose_name="Подкатегория", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Articles, self).save(*args, **kwargs)

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

