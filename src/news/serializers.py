from news.models import Article
from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault


class ArticleSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    last_update_by = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        read_only_fields = ('author', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'

    def get_last_update_by(self, obj):
        return obj.updated_by.full_name

    def get_author(self, obj):
        return obj.author.full_name
