from django.dispatch import receiver
from django.db.models.signals import post_save

from telegram_bot.bot import telegram_send
from telegram_bot.models import TelegramSupport, TelegramSpam
from telegram_bot.tasks import send_telegram_spam


@receiver(post_save, sender=TelegramSupport)
def signal_support(instance, created, **kwargs):
    if created:
        message = instance.message
        email = instance.email
        data = instance.data
        chat_id = '527164736'
        send_message = f'{email}\n{message}\n\n{data}'
        telegram_send(chat_id, send_message)


@receiver(post_save, sender=TelegramSpam)
def signal_telegram_spam(instance, created, **kwargs):
    if created:
        message = instance.message
        # image = instance.image
        print(message)
        send_telegram_spam(message)


