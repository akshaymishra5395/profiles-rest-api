from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test Api view"""
    serializers_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIview features"""
        an_apiview = [
            'Uses Http methods as function (get ,put, post and delete)',
            'is similar to tradistional django view ',
            'gives u the most controll over you application logic',
            'Is mapped ,anually t urls',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,status,
            status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle a delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializers_class = serializers.HelloSerializer

    def list(self,request):
        """Return a Hello message"""
        a_viewset=[
            'Uses action (list,create,retrive ,update ,partial_update)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message':"Hello!",'a_viewset':a_viewset})
    
    def create(self,request):
        """create a new Hello message"""
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response(
            {"http_method":'GET'}
        )
    def update(self,request,pk=None):
        """update a new Hello message"""
        return Response(
            {"http_method":'update'}
        )
    
    def delete(self,request,pk=None):
        """delete a new Hello message"""
        return Response(
            {"http_method":'Delete'}
        )
    
class UserProfileViewset(viewsets.ModelViewSet):
    """Handle cretaing and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentocation tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
        # IsAuthenticatedOrReadOnly,
    )

    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)