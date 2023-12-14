from django.urls import path

from telegram_bot.bot import set_webhook, telegram_webhook
from telegram_bot.views import telegram_link, support

urlpatterns = [
    path('webhook/', telegram_webhook, name='telegram_webhook'),
    path('set_webhook/', set_webhook, name='set_webhook'),
    path('telegram/', telegram_link, name='telegram_link'),
    path('support/', support, name='support'),

    ]