from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    imagesA = serializers.CharField(max_length=200)
    imagesI = serializers.CharField(max_length=200)
    cuisines = serializers.CharField(max_length=200)
    nom = serializers.CharField(max_length=200)
    prix = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    web = serializers.CharField(max_length=200)
    adresse = serializers.CharField(max_length=200)
    class Meta:
        model = Restaurant
        fields = ('imagesA', 'imagesI', 'cuisines','nom','prix','phone','web','adresse','menu',)
