from rest_framework import serializers

from ratings.models import Rating
from users.models import User
from .models import Restaurant


class RestaurantsListAPIViewSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'image', 'rating']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class RatingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Rating
        fields = ['stars', 'comment', 'customer', 'created_at']


class RestaurantRatingsListAPIViewSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'rating', 'ratings', 'image']
