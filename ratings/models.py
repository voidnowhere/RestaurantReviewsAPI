from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from restaurants.models import Restaurant
from users.models import User


class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name='ratings')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ratings')
    stars = models.SmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
