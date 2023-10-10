from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from product.serializers import ManufacturerSerializer, OrdersSerializer
from users.permissions import IsActive, IsCustomer

from product.models import Manufacturer, Orders


class ManufacturerListAPIView(ListAPIView):
    """ List для модели Manufacturer """

    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        queryset = Manufacturer.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class ManufacturerCreateAPIView(CreateAPIView):
    """ Create для модели Manufacturer """

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ManufacturerRetrieveAPIView(RetrieveAPIView):
    """ Retrieve для модели Manufacturer """

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ManufacturerUpdateAPIView(UpdateAPIView):
    """ Update для модели Manufacturer """

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ManufacturerDestroyAPIView(DestroyAPIView):
    """ Destroy для модели Manufacturer """

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class OrdersListAPIView(ListAPIView):
    """ List для модели Orders """

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class OrdersCreateAPIView(CreateAPIView):
    """ Create для модели Orders """

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class OrdersRetrieveAPIView(RetrieveAPIView):
    """ Retrieve для модели Orders """

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class OrdersUpdateAPIView(UpdateAPIView):
    """ Update для модели Orders """

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsCustomer]


class OrdersDestroyAPIView(DestroyAPIView):
    """ Destroy для модели Orders """

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
