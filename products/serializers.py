from rest_framework import serializers
import random


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(source="title", read_only=True)
    price = serializers.FloatField()
    image = serializers.URLField()
    stock = serializers.SerializerMethodField()

    def get_stock(self, obj) -> int:
        return random.randint(0, 150)
