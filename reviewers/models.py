from django.db import models

from users.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Restaurant(models.Model):
    cuisines = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    meals = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    longitude = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)


class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.SmallIntegerField()
    comment = models.CharField(max_length=2000)
    when = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
