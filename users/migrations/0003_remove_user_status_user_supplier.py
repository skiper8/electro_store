# Generated by Django 4.2.5 on 2023-10-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_status_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='supplier',
            field=models.BooleanField(default=False, verbose_name='статус'),
        ),
    ]
