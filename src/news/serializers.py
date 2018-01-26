from news.models import Article
from rest_framework import serializers


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = serializers.ALL_FIELDS
