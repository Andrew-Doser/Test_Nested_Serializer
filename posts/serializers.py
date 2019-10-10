from rest_framework import serializers
from .models import post
from statuses.models import status
from statuses.serializers import StatusSerializer, PostStatusSerializer



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = [
            'id',
            'title',
            'description',
            'status',
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = StatusSerializer(
            status.objects.get(pk=data['status'])).data
        return data

class TestSerializer(serializers.ModelSerializer):
    status_info = PostStatusSerializer(source='status', read_only=True)
    class Meta:
        model = post
        fields = [
            'id',
            'title',
            'description',
            'status',
            'status_info',
        ]