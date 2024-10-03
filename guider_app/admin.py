from django.contrib import admin
from .models import City, Street, Shop

class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'house_number', 'opening_time', 'closing_time')
    list_filter = ('city', 'street')
    search_fields = ('name', 'house_number')

# Регистрация с кастомными админ-классами
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(Shop, ShopAdmin)

