# Generated by Django 4.2.5 on 2023-10-09 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_orders_product_delete_individualentrepreneur_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ('country', 'city', 'status'), 'verbose_name': 'производитель', 'verbose_name_plural': 'производители'},
        ),
    ]
