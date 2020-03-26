from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers
from . import models
from rest_framework import status

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
