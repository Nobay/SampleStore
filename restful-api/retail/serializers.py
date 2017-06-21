from rest_framework import serializers

from retail.models import Asset, Category, Product


class AssetSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Asset
        fields = ("product", "image_url")


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Store model """
    class Meta:
        model = Category
        fields = ("name", "description")


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Product
        fields = ("category", "name", "description", "price")
