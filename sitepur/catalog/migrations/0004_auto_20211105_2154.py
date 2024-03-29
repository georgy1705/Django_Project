# Generated by Django 3.2.3 on 2021-11-05 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.gender', verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=10, verbose_name='Размер'),
        ),
    ]
