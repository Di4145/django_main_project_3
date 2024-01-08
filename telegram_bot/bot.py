import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from telebot import types

from shop.models import Type, Product
from telegram_bot.models import TelegramUser

telegram_api_key = settings.TELEGRAM_API_KEY
telegram_webhook_url = settings.TELEGRAM_WEBHOOK
bot = telebot.TeleBot(telegram_api_key)


def set_webhook(request):
    bot.remove_webhook()
    bot.set_webhook(telegram_webhook_url)
    return HttpResponse(f'<h1>Webhook set on {telegram_webhook_url}</h1>')


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse('Bot live')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Category')
    item2 = types.KeyboardButton('info2')
    markup.row(item1)
    markup.row(item2)
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}', reply_markup=markup)
    new_user = TelegramUser()
    new_user.chat_id = message.chat.id
    new_user.first_name = message.chat.first_name
    if message.chat.username is not None:
        new_user.username = message.chat.username
    try:
        new_user.django_user_id = message.text.split()[1]
        TelegramUser.objects.filter(chat_id=message.chat.id).update(django_user_id=message.text.split()[1])
    except:
        pass
    new_user.save()


@bot.message_handler(func=lambda message: message.text == 'Category')
def category(message):
    categorys = Type.objects.all()
    markup = types.InlineKeyboardMarkup()
    for category in categorys:
        button = types.InlineKeyboardButton(str(category), callback_data=f'category:{str(category)}')
        markup.add(button)
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('category'))
def detail_category(call):
    bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}')
    product_bot = call.data.split(':')[1]
    products = Product.objects.filter(type__name=product_bot)
    for product in products:
        bot.send_message(call.message.chat.id, f'{product} - {settings.HOST_URL}{product.get_absolute_url()}')



def telegram_send(chat_id, message):
    bot.send_message(chat_id, message)