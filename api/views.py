from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.serializers import ArticleSerializers, ProductSerializers, AuthorSerializers, LikeSerializers
from blog.models import Article, Like
from shop.models import Product


# Create your views here.
class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializers
    queryset = User.objects.all()


class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    # permission_classes = [IsAuthenticated]


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]