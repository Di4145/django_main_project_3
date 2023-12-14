from django.urls import path
from blog.views import blog, detail, like, favorites, article_edit

urlpatterns = [
    path('', blog, name='blog_page'),
    path('detail/<int:article_id>/', detail, name='article_detail'),
    path('like/', like, name='like_set'),
    path('favorites/', favorites, name='favorite_set'),
    path('article_edit/<int:id>/', article_edit, name='article_edit')

]
