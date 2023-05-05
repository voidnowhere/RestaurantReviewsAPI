from django.urls import path

from restaurants.views import RestaurantsVerificationListAPIView, RestaurantRetrieveAPIView, restaurant_verify

urlpatterns = [
    path('verification/', RestaurantsVerificationListAPIView.as_view()),
    path('verification/<int:pk>/', RestaurantRetrieveAPIView.as_view()),
    path('verification/<int:pk>/verify', restaurant_verify),
]
