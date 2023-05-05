from rest_framework import serializers

from .models import *
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'cuisines', 'price_range', 'meals', 'address', 'latitude', 'longitude', 'phone_number',
                  'website']


class RestaurantSerializerId(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','cuisines']


class RatingSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    restaurant = RestaurantSerializerId()

    class Meta:
        model = Rating
        fields = ['id', 'restaurant', 'customer', 'stars', 'comment', 'when', 'is_verified']
