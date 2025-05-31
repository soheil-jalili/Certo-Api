from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Insights, HomeCommentModel
from home.serializers import InsightSerializer, CommentSerializer


class HomeView(APIView):
    def get(self, request):
        # Comments
        model_comments = HomeCommentModel.objects.all()
        serializer_comments = CommentSerializer(instance=model_comments, many=True)

        # Insights
        models_insights = Insights.objects.all()
        serializer_insights = InsightSerializer(instance=models_insights, many=True)

        return Response({
            'comments': serializer_comments.data,
            'insights': serializer_insights.data
        }, status=status.HTTP_200_OK)
