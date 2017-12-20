from rest_framework import serializers

from ...products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'pk',
            'name', 'description',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'pk',
            'category', 'name', 'description',
            'price',
        )
