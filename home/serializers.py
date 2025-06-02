from rest_framework import serializers

from home.models import InsightModel, HomeCommentModel, HomeHeaderModel, SocialModel, FreedomBackModel, \
    ApplicationLinksModel


class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCommentModel
        fields = '__all__'


class HomeHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderModel
        exclude = ['id']


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialModel
        exclude = ['id']


class ApplicationLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationLinksModel
        exclude = ['id']


class FreedomBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreedomBackModel
        fields = '__all__'
