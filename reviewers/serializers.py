from rest_framework import serializers

from ratings.models import Rating
from restaurants.models import Restaurant
from users.models import User


class RestaurantsListAPIViewSerializer(serializers.ModelSerializer):
    unverified_ratings_count = serializers.IntegerField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'image', 'is_verified', 'unverified_ratings_count']


class RestaurantRetrieveAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisines', 'description', 'city', 'address', 'phone_number', 'website']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class RatingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Rating
        fields = ['id', 'stars', 'comment', 'customer', 'created_at', 'is_verified']


class RestaurantRatingsListAPIViewSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'city', 'ratings']
