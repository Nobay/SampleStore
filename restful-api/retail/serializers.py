from django.contrib.auth import get_user_model
from rest_framework import serializers

from retail.models import Asset, Category, Product, Customer


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


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel    .objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "first_name", "last_name", "email")


class CustomerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Customer
        fields = UserSerializer.Meta.fields + ('address', 'phone_number')

    def create(self, validated_data):
        customer = Customer    .objects.create(
            username=validated_data['username']
        )
        customer.set_password(validated_data['password'])
        customer.first_name = validated_data['first_name']
        customer.last_name = validated_data['last_name']
        customer.email = validated_data['email']
        customer.address = validated_data['address']
        customer.phone_number = validated_data['phone_number']
        customer.save()

        return customer
