from celery import shared_task

from telegram_bot.bot import bot
from telegram_bot.models import TelegramUser, TelegramSpam


@shared_task()
def send_telegram_spam(message):
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.chat_id, message)
        with open('media/telegram_spam/orig_2.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(user.chat_id, photo)


