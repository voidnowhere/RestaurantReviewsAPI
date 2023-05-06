from django.urls import path

from .views import RestaurantsListAPIView, RestaurantWithRatingsRetrieveAPIView

urlpatterns = [
    path('', RestaurantsListAPIView.as_view()),
    path('<int:id>/', RestaurantWithRatingsRetrieveAPIView.as_view()),
]
