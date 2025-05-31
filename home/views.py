from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        return Response({

        }, status=status.HTTP_200_OK)
