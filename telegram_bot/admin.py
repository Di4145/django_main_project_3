from django.contrib import admin

from telegram_bot.models import TelegramUser, TelegramSupport

admin.site.register(TelegramUser)
admin.site.register(TelegramSupport)
