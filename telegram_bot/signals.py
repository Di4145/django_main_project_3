from django.dispatch import receiver
from django.db.models.signals import post_save

from telegram_bot.bot import telegram_send
from telegram_bot.models import TelegramSupport


@receiver(post_save, sender=TelegramSupport)
def signal_support(instance, created, **kwargs):
    if created:
        message = instance.message
        email = instance.email
        data = instance.data
        chat_id = '527164736'
        send_message = f'{email}\n{message}\n\n{data}'
        telegram_send(chat_id, send_message)




