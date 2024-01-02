from django.contrib.auth.models import User
from django.db import models


class TelegramUser(models.Model):
    chat_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    django_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class TelegramSupport(models.Model):
    message = models.TextField()
    email = models.EmailField()
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email}, {self.data}'


class TelegramSpam(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    image = models.ImageField(upload_to='telegram_spam')

    def __str__(self):
        return self.title
