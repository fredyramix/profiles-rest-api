from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """ Returns a list of API Features"""
        an_apiview = [
        'Uses Http methos as fuction {get,post,patch,delete}',
        'Is similar to a traditiona Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','an_apiview':'an_apiview'})
