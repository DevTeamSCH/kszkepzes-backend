from news.permissions import IsStaffOrReadOnlyForAuthenticated
from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleListSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerializer
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]
    queryset = Article.objects.all()
