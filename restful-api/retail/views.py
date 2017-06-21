from rest_framework import viewsets
from retail.models import Asset, Category, Product
from retail.serializers import AssetSerializer, CategorySerializer, ProductSerializer


class AssetViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
