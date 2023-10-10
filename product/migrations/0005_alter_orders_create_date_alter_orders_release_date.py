# Generated by Django 4.2.5 on 2023-10-10 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_delete_product_alter_manufacturer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 19, 39, 46, 921909), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 10, 19, 39, 46, 921909), verbose_name='дата выхода продукта на рынок'),
        ),
    ]