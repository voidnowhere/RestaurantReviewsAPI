from django.shortcuts import render
from rest_framework.generics import *

from reviewers.models import Rating
from reviewers.serializers import *


# Create your views here.


class RatingListAPIView(ListAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()


class RestaurantListAPIView(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
