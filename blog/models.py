from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True, null=True)
    text_1 = models.TextField()
    photo = models.ImageField(upload_to='article_image', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Favorites(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)