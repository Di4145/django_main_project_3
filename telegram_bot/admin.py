from django.contrib import admin

from telegram_bot.models import TelegramUser, TelegramSupport, TelegramSpam

admin.site.register(TelegramUser)
admin.site.register(TelegramSupport)
admin.site.register(TelegramSpam)