from rest_framework import serializers

from restaurants.models import Restaurants


class RestaurantsVerificationSerializerListAPIView(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'name', 'image', 'latitude', 'longitude', 'is_verified']


class RestaurantsSerializerRetrieveAPIView(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['name', 'cuisines', 'price_range', 'meals', 'address', 'latitude', 'longitude',
                  'phone_number', 'website']
