# Generated by Django 3.1.5 on 2021-01-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(height_field=100, upload_to='thing_logos', width_field=100)),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
            ],
        ),
    ]
