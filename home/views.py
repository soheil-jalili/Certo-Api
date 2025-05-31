from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Insights, HomeCommentModel, HomeHeaderModel
from home.serializers import InsightSerializer, CommentSerializer, HomeHeaderSerializer


class HomeView(APIView):
    def get(self, request):
        # Home Header Model
        model_home_header_model = HomeHeaderModel.objects.all().last()
        serializer_home_header = HomeHeaderSerializer(instance=model_home_header_model)

        # Comments
        model_comments = HomeCommentModel.objects.all()
        serializer_comments = CommentSerializer(instance=model_comments, many=True)

        # Insights
        models_insights = Insights.objects.all()
        serializer_insights = InsightSerializer(instance=models_insights, many=True)

        return Response({
            'home_header_model': serializer_home_header.data,
            'comments': serializer_comments.data,
            'insights': serializer_insights.data
        }, status=status.HTTP_200_OK)


class CommentView(APIView):
    def post(self, request):
        serializer_comment = CommentSerializer(data=request.data)
        if serializer_comment.is_valid():
            serializer_comment.save()
            return Response({
                'message': 'Comment successfully Send',
                'comment': serializer_comment.data,
            }, status=status.HTTP_200_OK)
        return Response(serializer_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model_comments = HomeCommentModel.objects.filter(id=pk)
        model_comments.delete()
        return Response({
            'message': 'Comment Deleted'
        }, status=status.HTTP_200_OK)
