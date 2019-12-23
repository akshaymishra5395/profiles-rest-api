from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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

