# Generated by Django 3.2.3 on 2021-11-16 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20211116_1319'),
        ('catalog', '0008_alter_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer', verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_products', to='catalog.CartProduct'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer', verbose_name='Покупатель'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
