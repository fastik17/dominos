from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from dominos.mixins import ListSerializerMixin
from dominos.paginators import ResultPagination
from orders.models import Order
from orders import serializers


class OrderViewSet(ListSerializerMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    list:
    Get list of user's Orders

    Get list of user's Orders

    retrieve:
    Retrieve user's Order

    Retrieve user's Order

    create:
    Create Order object with pizzas

    Create Order object with pizzas

    update:
    Update Order with ID

    Update Order with the given ID.

    partial_update:
    Partial update of Order with ID

    Partial update of Order with ID

    destroy:
    Delete Order object with pizzas

    Delete Order object with pizzas
    """
    permission_classes = (IsAuthenticated,)
    list_serializer_class = serializers.OrderListSerializer
    serializer_class = serializers.OrderSerializer
    pagination_class = ResultPagination
    queryset = Order.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('status', 'customer')

    def perform_create(self, serializer):
        customer = self.request.user
        serializer.save(customer=customer)


class StatusViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    list:
    Get list of orders Status

    Get list of orders Status

    retrieve:
    Retrieve order Status

    Retrieve order Status

    update:
    Update Order status with ID

    Update Order status with the given ID.

    partial_update:
    Partial update of Order status with ID

    Partial update of Order status with ID
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.StatusSerializer
    pagination_class = ResultPagination
    queryset = Order.objects.all()
