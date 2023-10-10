from datetime import datetime

from django.db import models

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class Manufacturer(models.Model):
    """ Модель компаний """

    COMPANY_STATUS = [
        ('FACTORY', 'завод'),
        ('IE', 'ИП'),
        ('RETAIL', 'розничная сеть'),
    ]
    company_name = models.CharField(max_length=100, verbose_name='компания', **NULLABLE)
    status = models.CharField(choices=COMPANY_STATUS, verbose_name='статус', default='ИП')
    contact_email = models.EmailField(max_length=200, verbose_name='email производителя', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=200, verbose_name='улица', **NULLABLE)
    home_number = models.CharField(max_length=10, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return f'Компания {self.company_name} в статусе {self.status}'

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
        ordering = ('country', 'city', 'status')


class Orders(models.Model):
    """ Модель заказа """

    product_name = models.CharField(max_length=200, verbose_name='продукт', **NULLABLE)
    product_model = models.CharField(max_length=200, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    supplier = models.ForeignKey(Manufacturer, verbose_name='поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField(max_digits=15, default=0, decimal_places=2, verbose_name='задолжность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'Продукт {self.product_name} - {self.product_model}. Поставщик {self.supplier}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('product_name', 'release_date', 'create_date')
