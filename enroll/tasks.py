from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail 

@shared_task(bind=True)
def send_email_func1(self,subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)
    return "EXCUTE THE METHOND 1"


@shared_task()
def hello():
    print("hello")
    return "bye bye!!!!!!"