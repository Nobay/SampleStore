from rest_framework.routers import DefaultRouter
from retail.views import CategoryViewSet, AssetViewSet, ProductViewSet, get_auth_token, UserViewSet, \
    CustomerViewSet
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    # Session Login
    url(r'^login/$', get_auth_token, name='login'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = DefaultRouter()
router.register(prefix='categories', viewset=CategoryViewSet, base_name="my_categories")
router.register(prefix='assets', viewset=AssetViewSet, base_name="my_assets")
router.register(prefix='products', viewset=ProductViewSet, base_name="my_products")
router.register(prefix='users', viewset=UserViewSet, base_name="my_users")
router.register(prefix='customers', viewset=CustomerViewSet, base_name="my_customers")
urlpatterns += router.urls
