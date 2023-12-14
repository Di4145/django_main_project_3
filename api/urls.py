from django.urls import path, include
from rest_framework import routers
from api.views import ArticleModelViewSet, ProductModelViewSet, AuthorViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register('article', ArticleModelViewSet)
router.register('product', ProductModelViewSet)
router.register('author', AuthorViewSet)
router.register('like', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),

]