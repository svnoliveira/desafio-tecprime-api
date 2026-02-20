import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

EXTERNAL_API_URL = "https://fakestoreapi.com/products"


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        response = requests.get(EXTERNAL_API_URL)

        if response.status_code != 200:
            return Response(
                {"error": "Failed to fetch products"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        serializer = ProductSerializer(response.json(), many=True)

        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_id):
        response = requests.get(f"{EXTERNAL_API_URL}/{product_id}")

        if response.status_code == 404:
            return Response({"error": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch product"},
                            status=status.HTTP_502_BAD_GATEWAY)

        serializer = ProductSerializer(response.json())
        return Response(serializer.data)
