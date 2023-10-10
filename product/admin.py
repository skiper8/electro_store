from django.contrib import admin
from product.models import Manufacturer, Orders


@admin.action(description="сбросить долг до 0")
def reset_debt(modeladmin, request, queryset):
    """ Добавлена admin action, которая позволяет сбросить долг до 0 """
    queryset.update(debt=0)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    """ Модель Manufacturer в админке """

    list_display = ('id', 'company_name', 'status', 'country', 'city')
    list_filter = ('country', 'city')
    ordering = ('country', 'city')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """ Модель Orders в админке """

    list_display = ('id', 'product_name', 'product_model', 'release_date', 'supplier', 'debt', 'create_date')
    list_filter = ('product_name', 'product_model', 'supplier')
    ordering = ('debt', 'release_date', 'create_date')
    actions = [reset_debt]
