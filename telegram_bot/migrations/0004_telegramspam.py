# Generated by Django 4.2.5 on 2024-01-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0003_telegramsupport'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramSpam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='telegram_spam')),
            ],
        ),
    ]