from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurants', null=True, blank=True)
    cuisines = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=2500)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
