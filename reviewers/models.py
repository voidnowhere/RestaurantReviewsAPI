from django.db import models

from users.models import User


# Create your models here.
class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.email


class Restaurant(models.Model):
    cuisines = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    meals = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)


class Rating(models.Model):
    stars = models.SmallIntegerField()
    comment = models.CharField()
    when = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
