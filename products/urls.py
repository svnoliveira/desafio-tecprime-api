from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:product_id>/", ProductDetailView.as_view()),
]
