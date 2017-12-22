from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from news.models import Article
from news.serializers import ArticleListSerializer, ArticleDetailSerializer


class NewsListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAuthenticated]


class NewsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUser]
