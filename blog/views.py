from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import JsonResponse

from blog.forms import EditArticleForm
from blog.models import Article, Like, Favorites


# Create your views here.
def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    like_count = article.like_set.count()
    user_id = request.user.id
    if Like.objects.filter(user_id_id=user_id, article_id=article_id).exists():
        button = 'UnLike'
    else:
        button = 'Like'
    if Favorites.objects.filter(user_id_id=user_id, article_id=article_id).exists():
        button_2 = 'Удалить из избранного'
    else:
        button_2 = 'Добавить в избранное'
    return render(request, 'article_detail.html', {'article': article, 'like_count': like_count, 'button': button, 'button_2': button_2})


def like(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        article_id = request.POST['article_id']
        article = Article.objects.get(id=article_id)
        if Like.objects.filter(user_id_id=user_id, article_id=article_id).exists():
            new_like = Like.objects.filter(user_id_id=user_id, article_id=article_id)
            new_like.delete()
            button_label = 'Like'

        else:
            new_like = Like(user_id_id=user_id, article_id=article_id)
            new_like.save()
            button_label = 'UnLike'
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    like_count = article.like_set.count()
    return JsonResponse({'like_count': like_count, 'button_label': button_label})


def favorites(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        article_id = request.POST['article_id']
        if Favorites.objects.filter(user_id_id=user_id, article_id=article_id).exists():
            new_favorites = Favorites.objects.filter(user_id_id=user_id, article_id=article_id)
            new_favorites.delete()
            button_label_2 = 'Добавить в избранное'
        else:
            new_favorites = Favorites(user_id_id=user_id, article_id=article_id)
            new_favorites.save()
            button_label_2 = 'Удалить из избранного'
    return JsonResponse({'button_label_2': button_label_2})


def article_edit(request, id):
    if Article.objects.get(id=id).author == request.user:
        form = EditArticleForm(instance=Article.objects.get(id=id))
        return render(request, 'article_edit.html', {'form': form})
    else:
        return HttpResponse("Редактирование не возможно")
