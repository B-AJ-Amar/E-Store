# Generated by Django 4.2.3 on 2023-07-25 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_user_id_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderprod',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
