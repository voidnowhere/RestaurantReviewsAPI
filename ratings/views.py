from rest_framework.generics import CreateAPIView

from ratings.serializers import RatingCreateAPIViewSerializer
from users.permissions import IsCustomer


class RatingCreateAPIView(CreateAPIView):
    permission_classes = [IsCustomer]
    serializer_class = RatingCreateAPIViewSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
