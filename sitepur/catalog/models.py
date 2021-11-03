from django.db import models
from django.urls import reverse
from filer.fields.image import FilerImageField
from slugify import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField("Категория", unique=True, max_length = 50, db_index=True)
    slug = models.SlugField(max_length = 50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:catalog_home_by_category', args=[self.slug])

class Gender(models.Model):
    name = models.CharField("Пол", max_length = 20, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Subcategory(models.Model):
    name = models.CharField("Подкатегория", max_length = 20, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Brand(models.Model):
    name = models.CharField("Бренд", max_length = 20, db_index=True)

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

    title = models.CharField('Название', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание вещи')
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="products", on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, verbose_name="Пол", on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, verbose_name="Подкатегория", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Articles, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('catalog:shoes-detail', args=[self.id, self.slug])

class ArticlesImage(models.Model):
    post = models.ForeignKey(Articles, default=None, on_delete=models.CASCADE)
    img_detail = models.ImageField('Фотографии модели', upload_to='sneakers_img')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Фотография модели'
        verbose_name_plural = 'Фотографии модели кроссовок'

class Size(models.Model):
    post = models.ForeignKey(Articles, default=None, on_delete=models.CASCADE)
    size = models.CharField('Размер', max_length=10)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Размер модели'
        verbose_name_plural = 'Размеры моделей'
