from django.urls import path, include
from .views import (
    StatusViewSet
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'list', StatusViewSet, base_name='Status')

app_name='statuses' #Needed to run tests

#This is your endpoint API
urlpatterns = [
    path('', include(router.urls)),
]