from django.db import models
from filer.fields.image import FilerImageField
from slugify import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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


