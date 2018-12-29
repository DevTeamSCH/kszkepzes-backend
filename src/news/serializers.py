from news.models import Article
from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault


class ArticleSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    last_updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Article
        read_only_fields = ('author', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'

    def get_last_updated_by(self, obj):
        return obj.updated_by.id
