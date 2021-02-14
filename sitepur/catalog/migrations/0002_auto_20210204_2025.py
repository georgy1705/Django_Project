# Generated by Django 3.1.5 on 2021-02-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Все кроссовки', 'verbose_name_plural': 'Кроссовки'},
        ),
        migrations.AddField(
            model_name='articles',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание вещи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='img_detail',
            field=models.ImageField(default=1, upload_to='sneakers_logos_details'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(upload_to='sneakers_logos'),
        ),
    ]