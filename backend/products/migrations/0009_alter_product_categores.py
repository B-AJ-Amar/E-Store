# Generated by Django 4.2.3 on 2023-07-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categores',
            field=models.ManyToManyField(blank=True, null=True, related_name='prodcuts', to='products.category'),
        ),
    ]
