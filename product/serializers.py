from rest_framework.serializers import ModelSerializer
from product.models import Manufacturer, Orders


class ManufacturerSerializer(ModelSerializer):
    """ Serialiser для модели Manufacturer """

    class Meta:
        model = Manufacturer
        fields = '__all__'


class OrdersSerializer(ModelSerializer):
    """ Serialiser для модели Orders """

    class Meta:
        model = Orders
        fields = '__all__'
