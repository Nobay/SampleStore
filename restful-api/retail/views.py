from rest_framework import viewsets
from retail.models import Asset, Category, Product
from retail.serializers import AssetSerializer, CategorySerializer, ProductSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(AssetViewSet, self).get_serializer(*args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(CategoryViewSet, self).get_serializer(*args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ProductViewSet, self).get_serializer(*args, **kwargs)
