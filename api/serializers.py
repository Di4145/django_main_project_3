from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Article, Like
from shop.models import Product


class LikeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['article', 'user_id']


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ArticleSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'text', 'created_at', 'update', 'text_1', 'photo', 'like_count']

    @staticmethod
    def get_like_count(obj):
        return obj.like_set.count()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'maker', 'left', 'type', 'info', 'cover', 'on_site', 'sale']
