from django.shortcuts import render

from django.conf import settings

from telegram_bot.forms import SupportForm


def telegram_link(request):
    telegram_bot_link = settings.TELEGRAM_BOT_LINK
    link2 = f'{telegram_bot_link}?start={request.user.id}'
    return render(request, 'telegram.html', {'telegram_bot_link': telegram_bot_link, 'link2': link2})


def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupportForm()
    return render(request, 'support.html', {'form': form})