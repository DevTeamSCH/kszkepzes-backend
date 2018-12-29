from common.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Article.objects.all().order_by('-created_at')
