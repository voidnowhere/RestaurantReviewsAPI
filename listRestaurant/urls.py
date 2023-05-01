from django.urls import path
from .views import *


urlpatterns = [
    path('', RestaurantView.as_view(), name='Restaurant'),
    path('list/', RestaurantListView.as_view(), name='Restaurant'),
]
