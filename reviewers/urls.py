from django.urls import path

from .views import RestaurantsListAPIView, RestaurantRetrieveAPIView, rating_verify, restaurant_verify, \
    RestaurantWithRatingsRetrieveAPIView

urlpatterns = [
    path('restaurants/', RestaurantsListAPIView.as_view()),
    path('restaurants/<int:id>/', RestaurantRetrieveAPIView.as_view()),
    path('restaurants/<int:id>/verify', restaurant_verify),
    path('restaurants/<int:id>/ratings/', RestaurantWithRatingsRetrieveAPIView.as_view()),
    path('ratings/<int:id>/verify', rating_verify),
]
