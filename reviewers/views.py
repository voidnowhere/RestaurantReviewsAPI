from django.db.models import Count, Q, Prefetch
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from ratings.models import Rating
from restaurants.models import Restaurant
from users.permissions import IsReviewer
from .serializers import RestaurantsListAPIViewSerializer, RestaurantRetrieveAPIViewSerializer, \
    RestaurantRatingsListAPIViewSerializer


class RestaurantsListAPIView(ListAPIView):
    permission_classes = [IsReviewer]
    serializer_class = RestaurantsListAPIViewSerializer

    def get_queryset(self):
        return Restaurant.objects.annotate(
            unverified_ratings_count=Count('ratings', filter=Q(ratings__is_verified=False))
        ).order_by('-unverified_ratings_count').filter().all()


class RestaurantRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantRetrieveAPIViewSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsReviewer]
    lookup_field = 'id'


@api_view(['PATCH'])
@permission_classes([IsReviewer])
def restaurant_verify(request, id):
    restaurant = Restaurant.objects.filter(id=id).first()
    if not restaurant:
        return NotFound
    restaurant.is_verified = not restaurant.is_verified
    restaurant.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsReviewer])
def rating_verify(request, id):
    try:
        rating = Rating.objects.get(id=id)
    except Rating.DoesNotExist:
        return NotFound
    rating.is_verified = not rating.is_verified
    rating.save()
    return Response(status=status.HTTP_200_OK)


class RestaurantWithRatingsRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantRatingsListAPIViewSerializer
    queryset = Restaurant.objects.prefetch_related(
        Prefetch('ratings', queryset=Rating.objects.order_by('created_at'))
    ).all()
    permission_classes = [IsReviewer]
    lookup_field = 'id'
