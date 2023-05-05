from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response

from reviewers.serializers import *


# Create your views here.


@api_view(['PATCH'])
def update_rating_is_verified(request, id):
    try:
        rating = Rating.objects.get(id=id)
    except Rating.DoesNotExist:
        return Response({'detail': 'Rating not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RatingSerializer(rating, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class RatingListAPIView(ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['id']
        if restaurant_id:
            return Rating.objects.filter(restaurant_id=restaurant_id)
        return Rating.objects.all()


class RestaurantListAPIView(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
