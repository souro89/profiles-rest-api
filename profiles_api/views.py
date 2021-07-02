from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Resturns a list of APIView features"""

        an_apiview=[
            'Uses HTTP methods as function',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        message = f'Hello , {name}'

        return Response({'message':message})

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    
    def patch(self, request, pk=None):
        """handle partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """handle delete an object"""
        return Response({'method':'DELETE'})
