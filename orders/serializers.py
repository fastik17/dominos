from django.db import transaction
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from orders.models import Pizza, Order
from authentication.serializers import CurrentUserSerializer


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('id', 'flavor', 'size', 'quantity')


class OrderListSerializer(serializers.ModelSerializer):
    customer = CurrentUserSerializer()

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_address', 'status')
        read_only_fields = ('id', 'customer')


class OrderSerializer(WritableNestedModelSerializer):
    pizza = PizzaSerializer(many=True)
    customer = CurrentUserSerializer()

    class Meta:
        model = Order
        fields = ('id', 'pizza', 'customer', 'customer_address', 'status', 'created_at')
        read_only_fields = ('id', 'customer')

    @transaction.atomic
    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        order = super().create(validated_data)
        return order


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status')
        read_only_fields = ('id',)
