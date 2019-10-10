from rest_framework import serializers
from .models import status



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = [
            'id',
            'name',
        ]

class PostStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = [
            'name',
        ]