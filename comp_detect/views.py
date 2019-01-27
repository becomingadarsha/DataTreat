from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "comp_detect/index.html")

def treatment(request):
    return render(request, "comp_detect/treatment.html")

def contact(request):
    return render(request, "comp_detect/contact.html")
