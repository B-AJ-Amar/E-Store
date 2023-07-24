# Generated by Django 4.2.3 on 2023-07-24 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_photo_product_id_photo_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poduct_p', to='products.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]