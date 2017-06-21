from rest_framework import serializers

from retail.models import Asset, Category, Product


class AssetSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Asset
        fields = ("id", "product", "image_url")


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    assets = AssetSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "assets")


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Store model """
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "description", "products")
