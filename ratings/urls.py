from django.urls import path

from .views import RatingCreateAPIView

urlpatterns = [
    path('', RatingCreateAPIView.as_view()),
]
