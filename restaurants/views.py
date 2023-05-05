from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantsVerificationListAPIViewSerializer, \
    RestaurantVerificationRetrieveAPIViewSerializer
from users.permissions import IsReviewer


class RestaurantsVerificationListAPIView(ListAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = [IsReviewer]
    serializer_class = RestaurantsVerificationListAPIViewSerializer


class RestaurantRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantVerificationRetrieveAPIViewSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsReviewer]
    lookup_field = 'pk'


@api_view(['PATCH'])
@permission_classes([IsReviewer])
def restaurant_verify(request, pk):
    restaurant = Restaurant.objects.filter(pk=pk).first()
    if not restaurant:
        return NotFound
    restaurant.is_verified = not restaurant.is_verified
    restaurant.save()
    return Response(status=status.HTTP_200_OK)
