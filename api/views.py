from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

class LinksView(APIView):
    def get(self, request):
        return Response(status.HTTP_200_OK)
