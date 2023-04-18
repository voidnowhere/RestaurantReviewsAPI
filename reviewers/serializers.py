from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [ 'name']


class RatingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'restaurant', 'customer', 'stars', 'comment', 'when', 'is_verified']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'cuisines', 'price_range', 'meals', 'address', 'latitude', 'longitude', 'phone_number', 'website']
