from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    cuisines = serializers.CharField(max_length=100)
    price_range = serializers.CharField(max_length=100)
    meals = serializers.CharField(max_length=100)
    adresse = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    website = serializers.CharField(max_length=100)

    class Meta:
        model = Restaurant
        fields = ('cuisines', 'price_range', 'meals', 'adresse', 'phone_number', 'website',)
