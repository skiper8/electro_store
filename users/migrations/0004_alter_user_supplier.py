# Generated by Django 4.2.5 on 2023-10-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_status_user_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='supplier',
            field=models.BooleanField(default=False, verbose_name='поставщик'),
        ),
    ]