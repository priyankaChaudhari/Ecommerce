from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



from .models import (User)


class SignupView(APIView):
    """
    view to signup the user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
    
    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        a = User.objects.create_user(password=password, username=username)
        print(a,"!!!!")
        user = authenticate(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        #        token = Token.objects.create(user=user)
        #print("post @#######3", username, password, token)
        return Response({'token': token.key})
    

    # print(request.data,"inside post methos", request.user, "@@@", request.auth)
    #    return Response(request.data)

    # def get(self, request):
    #     print(User.objects.all())
    #     return Response(User.objects.all())

