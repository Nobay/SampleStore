from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from retail.models import Asset, Category, Product, Customer
from retail.permissions import UserPermission, ItemPermission
from retail.serializers import AssetSerializer, CategorySerializer, ProductSerializer, UserSerializer, \
    CustomerSerializer
from rest_framework.authtoken.models import Token


class UpdateModelMixin(object):
    """
    Update a model instance.
    """
    def partial_update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class AssetViewSet(UpdateModelMixin, viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [
        ItemPermission
    ]

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(AssetViewSet, self).get_serializer(*args, **kwargs)


class CategoryViewSet(UpdateModelMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        ItemPermission
    ]

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(CategoryViewSet, self).get_serializer(*args, **kwargs)


class ProductViewSet(UpdateModelMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        ItemPermission
    ]

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ProductViewSet, self).get_serializer(*args, **kwargs)


def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return redirect('/polls/', request)
    return redirect(settings.LOGIN_URL, request)


class UserViewSet(UpdateModelMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        UserPermission     # Only super user
    ]
    serializer_class = UserSerializer


class CustomerViewSet(UserViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
