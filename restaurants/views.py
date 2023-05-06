from django.db.models import Avg, Q, Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ratings.models import Rating
from .models import Restaurant
from .serializers import RestaurantsListAPIViewSerializer, RestaurantRatingsListAPIViewSerializer


class RestaurantsListAPIView(ListAPIView):
    serializer_class = RestaurantsListAPIViewSerializer

    def get_queryset(self):
        return Restaurant.objects.annotate(
            rating=Avg('ratings__stars', filter=Q(ratings__is_verified=True))
        ).filter(
            is_verified=True,
            name__contains=self.request.query_params.get('name', '')
        ).order_by('-rating').all()


class RestaurantWithRatingsRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantRatingsListAPIViewSerializer
    queryset = Restaurant.objects.prefetch_related(
        Prefetch('ratings', queryset=Rating.objects.filter(is_verified=True).order_by('-created_at'))
    ).annotate(
        rating=Avg('ratings__stars', filter=Q(ratings__is_verified=True)),
    ).filter(
        is_verified=True,
    ).all()
    lookup_field = 'id'
