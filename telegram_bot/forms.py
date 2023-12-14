from django import forms

from telegram_bot.models import TelegramSupport


class SupportForm(forms.ModelForm):
    class Meta:
        model = TelegramSupport
        fields = ['message', 'email']