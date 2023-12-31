# Generated by Django 4.2.5 on 2023-10-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='продукт')),
                ('product_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='модель')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='дата выхода продукта на рынок')),
            ],
        ),
        migrations.DeleteModel(
            name='IndividualEntrepreneur',
        ),
        migrations.DeleteModel(
            name='Suppliers',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='manufacturer_name',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='компания'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='home_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='номер дома'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='status',
            field=models.CharField(choices=[('FACTORY', 'завод'), ('IE', 'ИП'), ('RETAIL', 'розничная сеть')], default='ИП', verbose_name='статус'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='улица'),
        ),
    ]
