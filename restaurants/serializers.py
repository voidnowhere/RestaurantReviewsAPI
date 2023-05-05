from rest_framework import serializers

from restaurants.models import Restaurant


class RestaurantsVerificationListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'image', 'is_verified']


class RestaurantVerificationRetrieveAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisines', 'description', 'city', 'address', 'phone_number', 'website']
