from rest_framework import serializers
from .models import *


class RatestarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratestar
        fields = ('rate',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comments',)


class RestaurantSerializer(serializers.ModelSerializer):
    imagesA = serializers.CharField(max_length=200)
    imagesI = serializers.CharField(max_length=200)
    cuisines = serializers.CharField(max_length=200)
    nom = serializers.CharField(max_length=200)
    prix = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    web = serializers.CharField(max_length=200)
    adresse = serializers.CharField(max_length=200)
    comments = CommentSerializer(many=True, read_only=True)
    rate = RatestarSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('imagesA', 'imagesI', 'cuisines', 'nom', 'prix', 'phone', 'web', 'adresse', 'menu', 'comments', 'rate',)
