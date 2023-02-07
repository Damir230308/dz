from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, AuthorModelSerializer2, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

class MyAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer = AuthorModelSerializer
    
    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorModelSerializer
        return AuthorModelSerializer2