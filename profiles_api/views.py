from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api view"""

    def get(self,request,format=None):
        """Return a list of APIview features"""
        an_apiview = [
            'Uses Http methods as function (get ,put, post and delete)',
            'is similar to tradistional django view ',
            'gives u the most controll over you application logic',
            'Is mapped ,anually t urls',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

