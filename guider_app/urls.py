from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, StreetViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'city/(?P<city_id>[^/.]+)/street', StreetViewSet, basename='street')
router.register(r'shop', ShopViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls)),
]