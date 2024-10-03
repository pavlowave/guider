from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        if city_id:
            return super().get_queryset().filter(city_id=city_id)
        return super().get_queryset()


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            shop = serializer.save()

            # Возвращаем только id города
            response_data = {
                "id": shop.id,
            }
            return Response(response_data, status=201)

        except ValidationError as e:
            # Возвращаем ошибку валидации
            return Response({"errors": e.detail}, status=400)

        except Exception as e:
            # Возвращаем общую ошибку
            return Response({"error": str(e)}, status=400)

    def get_queryset(self):
        queryset = super().get_queryset()
        street = self.request.query_params.get('street')
        city = self.request.query_params.get('city')
        open_status = self.request.query_params.get('open')

        if street:
            queryset = queryset.filter(street__name__icontains=street)
        if city:
            queryset = queryset.filter(city__name__icontains=city)
        if open_status is not None:
            queryset = [shop for shop in queryset if shop.is_open() == (open_status == '1')]

        return queryset