# Generated by Django 4.2.5 on 2023-12-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0002_alter_telegramuser_chat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]