from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *

class AssetList(APIView):

    def get(self, request, format=None):

        Asset = AssetManagement.objects.all()
        serializer = AssestSerializer(Asset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = AssestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDetail(APIView):

    def get(self, request, format=None):

