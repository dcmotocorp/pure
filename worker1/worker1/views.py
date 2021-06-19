from django.shortcuts import render
import rest_framework
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from .serializers import UserSerializer 
from .models import User 

# Create your views here.

class UserApi(APIView):
    """   
    UserApi  used for the Crud operation of the  user 
    
    """ 
    def get(self,formate=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,formate=None):
        pass
    
    def put(self,formate=None):
        pass
    
    def update(self,formate=None):
        pass