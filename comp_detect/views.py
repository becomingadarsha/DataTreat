from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Message


def index(request):
    return render(request, "comp_detect/index.html")

def treatment(request):
    return render(request, "comp_detect/treatment.html")

def contact(request):
    return render(request, "comp_detect/contact.html")

@require_http_methods(['POST'])
def save_message(request):
    sender_name = request.POST.get('sender_name')
    sender_phone = request.POST.get('sender_phone')
    message = request.POST.get('message')

    new_message = Message()
    new_message.name = sender_name
    new_message.phone = sender_phone
    new_message.message = message
    new_message.save()

    return render(request, "comp_detect/message_send.html", context = {'name': sender_name})
