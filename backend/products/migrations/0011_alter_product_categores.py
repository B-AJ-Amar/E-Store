# Generated by Django 4.2.3 on 2023-07-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_categores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categores',
            field=models.ManyToManyField(blank=True, related_name='prodcuts', to='products.category'),
        ),
    ]
