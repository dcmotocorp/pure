from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from urllib.request import urlopen


 # Create your views here.
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
from drf_yasg import openapi
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from classadd.classadd import Post
post_object= Post()


class PostViewSet2(ViewSet):
    """
    A simple ViewSet for listing or retrieving post.
    """
    def list(self, request):
        list=post_object.list_objects()
        return Response(list)

    
    def retrieve(self, request, id=None):
        data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts/' + str(id)))
        return Response(data)





# class PostViewSet2(ViewSet):
#     """
#     A simple ViewSet for listing or retrieving post.
#     """
#     def list(self, request):
#         data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts'))
#         return Response(data)
    
#     def retrieve(self, request, id=None):
#         data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts/' + str(id)))
#         return Response(data)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)