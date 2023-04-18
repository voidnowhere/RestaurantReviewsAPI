from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from restaurants.models import Restaurants
from restaurants.serializers import RestaurantsVerificationSerializerListAPIView, RestaurantsSerializerRetrieveAPIView
from users.permissions import IsReviewer


class RestaurantsVerificationListAPIView(ListAPIView):
    queryset = Restaurants.objects.all()
    permission_classes = [IsReviewer]
    serializer_class = RestaurantsVerificationSerializerListAPIView


class RestaurantRetrieveAPIView(RetrieveAPIView):
    serializer_class = RestaurantsSerializerRetrieveAPIView
    queryset = Restaurants.objects.all()
    permission_classes = [IsReviewer]
    lookup_field = 'id'


@api_view(['PATCH'])
@permission_classes([IsReviewer])
def restaurant_verify(request, id):
    restaurant = Restaurants.objects.filter(id=id).first()
    if not restaurant:
        return NotFound
    restaurant.is_verified = not restaurant.is_verified
    restaurant.save()
    return Response(status=status.HTTP_200_OK)
