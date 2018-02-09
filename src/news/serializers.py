from news.models import Article
from rest_framework import serializers


class ArticleListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = serializers.ALL_FIELDS

    def get_author_name(self, obj):
        return obj.author.user.get_full_name()
