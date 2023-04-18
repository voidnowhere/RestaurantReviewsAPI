from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Restaurant
from .serializers import *


# Create your views here.

class RestaurantView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
