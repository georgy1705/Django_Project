# Generated by Django 3.1.7 on 2021-03-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20210320_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Суперпользователь с таким именем уже существует.'}, help_text='Максимальные длина 15 символов. Можно использовать @/./+/-/_', max_length=15, unique=True, verbose_name='Admin_name'),
        ),
    ]
