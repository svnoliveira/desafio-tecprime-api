from rest_framework import serializers
from order_products.serializers import OrderProductSerializer
from .models import Order
from order_products.models import OrderProduct


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "name",
            "email",
            "address",
            "payment",
            "created_at",
            "updated_at",
            "order_products",
        ]

    def create(self, validated_data: dict) -> Order:
        order_products = validated_data.pop("order_products")
        order = Order.objects.create(**validated_data)

        for product in order_products:
            OrderProduct.objects.create(**product, order=order)

        return order
