from django.db import models
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='streets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='shops', on_delete=models.CASCADE)
    street = models.ForeignKey(Street, related_name='shops', on_delete=models.CASCADE)
    house_number = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def is_open(self):
        now = timezone.localtime().time()
        # Проверяем, если магазин закрывается после полуночи
        if self.closing_time < self.opening_time:
            return now >= self.opening_time or now <= self.closing_time
        return self.opening_time <= now <= self.closing_time

    def __str__(self):
        return self.name
