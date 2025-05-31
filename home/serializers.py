from rest_framework import serializers

from home.models import Insights, HomeCommentModel, HomeHeaderModel


class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insights
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCommentModel
        fields = '__all__'


class HomeHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderModel
        exclude = ['id']
