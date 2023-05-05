from .views import *
from django.urls import path

urlpatterns = [
    path('ratings/<int:id>/', RatingListAPIView.as_view()),
    path('restaurant/', RestaurantListAPIView.as_view()),
    path('restaurant/<int:id>/ratings', update_rating_is_verified),

]