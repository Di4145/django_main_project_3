from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def spam(message, subject, email):
    message = message
    subject = subject
    email = email
    from_email = 'plotnikov-d@bk.ru'
    recepient = ['plotnikov_da@npcses.ru', email]
    for i in range(1, 5000):
        send_mail(subject, message, from_email, recepient)
