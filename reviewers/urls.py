from reviewers.views import *
from django.urls import path

urlpatterns = [
    path('rating/', RatingListAPIView.as_view()),
    path('restaurant/', RestaurantListAPIView.as_view()),

]