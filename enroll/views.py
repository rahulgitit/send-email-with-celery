from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from enroll.tasks import send_email_func1


print("welcome to my project")
def sendmail(request):
    subject = 'welcome to GFG world'
    message = f'Hi this function is used the testing perpose'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["rahulhaibatpur022@gmail.com"]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("email send successfuly!!!!!!!!!!")


def home(request):
    subject = 'welcome to GFG world'
    message = f'Hi this function is used the testing perpose'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["rahulhaibatpur022@gmail.com"]
    send_email_func1.delay( subject, message, email_from, recipient_list )
    return HttpResponse("email send successfuly!!!!!!!!!!")
    