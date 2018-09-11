from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.decorators import detail_route, list_route

class SignupView(APIView):
    """
    view to signup the user.
    """
    print("inside signup view")
