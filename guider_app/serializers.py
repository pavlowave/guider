from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    street_name = serializers.CharField(source='street.name', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house_number', 'opening_time', 'closing_time', 'city_name', 'street_name']

        # Убираем city и street из ответа, если они не нужны
        extra_kwargs = {
            'city': {'write_only': True},
            'street': {'write_only': True},
        }