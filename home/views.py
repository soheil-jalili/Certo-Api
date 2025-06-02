from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import InsightModel, HomeCommentModel, HomeHeaderModel, SocialModel, FreedomBackModel, \
    ApplicationLinksModel
from home.serializers import InsightSerializer, CommentSerializer, HomeHeaderSerializer, SocialSerializer, \
    ApplicationLinksSerializer, FreedomBackSerializer


class HomeView(APIView):
    def get(self, request):
        # Home Header Model
        model_home_header_model = HomeHeaderModel.objects.all().last()
        serializer_home_header = HomeHeaderSerializer(instance=model_home_header_model)

        # Comments
        model_comments = HomeCommentModel.objects.all()
        serializer_comments = CommentSerializer(instance=model_comments, many=True)

        # Insights
        model_insights = InsightModel.objects.all()[:3]
        serializer_insights = InsightSerializer(instance=model_insights, many=True)

        # Socials
        model_socials = SocialModel.objects.all()
        serializer_socials = SocialSerializer(instance=model_socials, many=True)

        # Application Links
        model_application = ApplicationLinksModel.objects.all()
        serializer_application = ApplicationLinksSerializer(instance=model_application, many=True)

        # FreedomBack
        model_freedom = FreedomBackModel.objects.all()[:6]
        serializer_socials = FreedomBackSerializer(instance=model_freedom, many=True)

        return Response({
            'home_header_model': serializer_home_header.data,
            'comments': serializer_comments.data,
            'freedom': serializer_socials.data,
            'application': serializer_application.data,
            'insights': serializer_insights.data,
            'socials': serializer_socials.data,
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


class SocialView(APIView):
    def put(self, request, pk):
        social_instance = get_object_or_404(SocialModel, id=pk)

        serializer_social = SocialSerializer(social_instance, data=request.data, partial=True)

        if serializer_social.is_valid():
            serializer_social.save()
            return Response({
                'message': 'Social Successfully Updated',
            }, status=status.HTTP_200_OK)
        return Response(serializer_social.errors, status=status.HTTP_400_BAD_REQUEST)


class AllInsights(APIView):
    def get(self, request):
        model_insights = InsightModel.objects.all()
        serializer_insights = InsightSerializer(instance=model_insights, many=True)

        return Response({
            'insights': serializer_insights.data,
        })


class InsightDetail(APIView):
    def get(self, request, slug):
        model_insights = InsightModel.objects.get(slug=slug)
        serializer_insights = InsightSerializer(instance=model_insights)
        return Response({
            'insight': serializer_insights.data,
        })


class AddInsight(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        insights_serializer = InsightSerializer(data=request.data)
        if insights_serializer.is_valid():
            if request.user.is_authenticated:
                insights_serializer.save(user=request.user)
                return Response({
                    'message': 'Insight Successfully Added',
                }, status=201)
            else:
                return Response({
                    'error': 'User is not authenticated',
                }, status=403)

        return Response({
            'error': insights_serializer.errors,
        }, status=400)


class UpdateInsight(APIView):
    pass


class RemoveInsight(APIView):
    pass
