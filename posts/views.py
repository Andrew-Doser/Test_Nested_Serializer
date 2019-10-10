from django.shortcuts import render
from .models import post
from .serializers import PostSerializer, TestSerializer
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404
import json

def is_json(json_data):
    """
    Purpose:
        Needed a function to validate json function.
        Probably could have done it with a serializer.
    Created By:
        Andrew Doser
        10/3/2019
    """
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid



class PostViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    #serializer_class = TestSerializer

class TestViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,):
    queryset = post.objects.all()
    #serializer_class = PostSerializer
    serializer_class = TestSerializer
# Create your views here.


