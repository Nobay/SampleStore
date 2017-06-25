from rest_framework import serializers

from retail.models import Asset, Category, Product


class NestedListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        pass

    def to_representation(self, data):
        r = super().to_representation(data)

        return {item['id'] for item in r}


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ("id", "product", "image_url")


class ListAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = ("id",)
        list_serializer_class = NestedListSerializer


class ProductSerializer(serializers.ModelSerializer):
    assets = ListAssetSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "assets")


class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id",)
        list_serializer_class = NestedListSerializer


class CategorySerializer(serializers.ModelSerializer):
    products = ListProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "description", "products")
