from django.db.models import Avg, Q, Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ratings.models import Rating
from .models import Restaurant
from .serializers import RestaurantsListAPIViewSerializer, RestaurantRatingsListAPIViewSerializer


class RestaurantsListAPIView(ListAPIView):
    queryset = Restaurant.objects.annotate(
        rating=Avg('ratings__stars', filter=Q(ratings__is_verified=True))
    ).filter(is_verified=True).all()
    serializer_class = RestaurantsListAPIViewSerializer


class RestaurantWithRatingsRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantRatingsListAPIViewSerializer
    queryset = Restaurant.objects.prefetch_related(
        Prefetch('ratings', queryset=Rating.objects.filter(is_verified=True).order_by('-created_at'))
    ).filter(
        is_verified=True,
    ).annotate(
        rating=Avg('ratings__stars', filter=Q(ratings__is_verified=True)),
    ).all()
    lookup_field = 'id'
