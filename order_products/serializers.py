from rest_framework import serializers

from .models import OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["id", "name", "amount", "shop_id"]
