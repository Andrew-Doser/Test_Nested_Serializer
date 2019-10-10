from django.urls import path, include
from .views import (
    TestViewSet,
    PostViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', PostViewSet, base_name='Post')
router.register(r'test', TestViewSet, base_name='Test')


app_name='posts' #Needed to run tests

#This is your endpoint API
urlpatterns = [
    path('', include(router.urls)),
]