from common.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Article.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        kwargs = {
            'author': self.request.user.profile,
            'updated_by': self.request.user.profile,
        }
 
        serializer.save(**kwargs)