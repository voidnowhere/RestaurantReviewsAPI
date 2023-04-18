from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurants')
    cuisines = models.CharField(max_length=255)
    price_range = models.CharField(max_length=100)
    meals = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_number = models.CharField(max_length=13)
    website = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
