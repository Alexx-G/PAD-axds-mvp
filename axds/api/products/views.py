from rest_framework.viewsets import ModelViewSet

from ...products.models import Category, Product
from .serializers import (
    CategorySerializer, ProductSerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('name', 'description')
    filter_fields = ('name',)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ('category__name', 'name', 'description')
    filter_fields = ('price',)
