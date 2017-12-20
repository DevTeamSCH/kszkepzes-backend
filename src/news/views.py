from rest_framework import generics
from models import Article
from news.serializer import ArticleListSerializer


class NewsListView(generics.ListAPIView):
    qureryset = Article.objects.all()
    serializer_class = ArticleListSerializer
