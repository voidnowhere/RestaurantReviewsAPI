from django.db import models


# Create your models here.
class Restaurant(models.Model):
    imagesA = models.CharField(max_length=200)
    imagesI = models.CharField(max_length=200)
    cuisines = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prix = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    web = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    menu = models.TextField()


