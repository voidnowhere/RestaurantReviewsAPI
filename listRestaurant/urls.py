from django.urls import path
from .views import *


urlpatterns = [
    path('', RestaurantView.as_view(), name='Restaurant'),
    path('list/', RestaurantListView.as_view(), name='Restaurant'),
    path('comment/<int:pk>/', get_comment),
    path('comments/<int:pk>/', create_comment),
]
