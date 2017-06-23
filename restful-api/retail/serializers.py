from rest_framework import serializers

from retail.models import Asset, Category, Product


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ("id", "product", "image_url")


class ProductSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "assets")


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "description", "products")
