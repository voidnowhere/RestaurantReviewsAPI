from django.db import models


# Create your models here.
class Restaurant(models.Model):
    cuisines = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    meals = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
