from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Book, Biography, Article


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'

class AuthorModelSerializer2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name']