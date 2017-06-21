from rest_framework.routers import DefaultRouter
from retail.views import CategoryViewSet, AssetViewSet, ProductViewSet

router = DefaultRouter()
router.register(prefix='categories', viewset=CategoryViewSet)
router.register(prefix='assets', viewset=AssetViewSet)
router.register(prefix='products', viewset=ProductViewSet)

urlpatterns = router.urls
