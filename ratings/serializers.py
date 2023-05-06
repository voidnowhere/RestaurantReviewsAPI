from rest_framework import serializers

from ratings.models import Rating


class RatingCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['comment', 'stars', 'restaurant']
