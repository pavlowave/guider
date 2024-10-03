from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, ShopViewSet, StreetViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'street', StreetViewSet, basename='street')
router.register(r'shop', ShopViewSet, basename='shop')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/city/<int:city_id>/street/', StreetViewSet.as_view({'get': 'list'}), name='city-street-list'),
]