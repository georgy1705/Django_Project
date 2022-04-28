# Generated by Django 3.2.3 on 2022-04-26 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0009_auto_20211116_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('img_detail', models.ImageField(upload_to='reviews_img', verbose_name='Фотографии модели для отзыва')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_articles', to='catalog.articles', verbose_name='Отзыв')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
            ],
        ),
    ]
