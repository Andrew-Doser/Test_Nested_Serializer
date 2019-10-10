from django.shortcuts import render
from .models import status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics
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


# Create your views here.
class StatusViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,):
    queryset = status.objects.all()
    serializer_class = StatusSerializer

