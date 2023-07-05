from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.urls import reverse

from home.models import Contact
from datetime import datetime


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_sub = request.POST['message-sub']
        message = request.POST['message']
        contact_no = request.POST['phno']

        con_db = Contact(
            name = message_name,
            email = message_email,
            subject = message_sub,
            message = message,
            contact_no = contact_no
        )
        con_db.save()

        # send mail

        send_mail(
            message_sub,
            message,
            message_email,
            [settings.EMAIL_HOST_USER],
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else: 
        return render(request, 'contact.html', {})
    

def detail(request):
    return render(request, 'detail.html', {})
