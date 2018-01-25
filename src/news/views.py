from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleListSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
