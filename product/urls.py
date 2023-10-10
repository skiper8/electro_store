from django.urls import path

from users.apps import UsersConfig
from product.views import ManufacturerListAPIView, ManufacturerCreateAPIView, ManufacturerRetrieveAPIView, \
    ManufacturerUpdateAPIView, ManufacturerDestroyAPIView, OrdersListAPIView, OrdersCreateAPIView, \
    OrdersRetrieveAPIView, OrdersUpdateAPIView, OrdersDestroyAPIView
from django.views.decorators.cache import never_cache

app_name = UsersConfig.name

urlpatterns = [
    # Manufacturer
    path('manufacturer/', ManufacturerListAPIView.as_view(), name='manufacturer-list'),
    path('manufacturer/create/', never_cache(ManufacturerCreateAPIView.as_view()), name='manufacturer-create'),
    path('manufacturer/<int:pk>/', ManufacturerRetrieveAPIView.as_view(), name='manufacturer-detail'),
    path('manufacturer/<int:pk>/update/', never_cache(ManufacturerUpdateAPIView.as_view()), name='manufacturer-update'),
    path('manufacturer/<int:pk>/delete/', never_cache(ManufacturerDestroyAPIView.as_view()),
         name='manufacturer-delete'),

    # Orders
    path('orders/', OrdersListAPIView.as_view(), name='orders-list'),
    path('orders/create/', never_cache(OrdersCreateAPIView.as_view()), name='orders-create'),
    path('orders/<int:pk>/', OrdersRetrieveAPIView.as_view(), name='orders-detail'),
    path('orders/<int:pk>/update/', never_cache(OrdersUpdateAPIView.as_view()), name='orders-update'),
    path('orders/<int:pk>/delete/', never_cache(OrdersDestroyAPIView.as_view()), name='orders-delete'),
]
