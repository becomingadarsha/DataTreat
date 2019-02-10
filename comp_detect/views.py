from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Message, Feature
from pydoc import locate
from django.forms.models import model_to_dict
from .ai import load_model
import numpy as np

def index(request):
    return render(request, "comp_detect/index.html")

def treatment(request):
    if(request.method == "POST"):
        complications = [
                "Cardiovascular disease",
                "Nerve Damage (Neuropathy)",
                "Kidney Damage (Nephropathy)",
                "Eye Damage (Retinopathy)",
                "Foot Damage",
                "Skin Conditions",
                "Hearing Impairment",
                "Alzheimer's Disease",
                "Depression"]
        sex = int(request.POST.get("sex"))
        medInTime = float(request.POST.get("medInTime"))
        age = int(request.POST.get("age"))
        timeSufDbt = float(request.POST.get("timeSufDbt"))
        avgDbtRate = int(request.POST.get("avgDbtRate"))
        type = int(request.POST.get("type"))
        otherProb = int(request.POST.get("otherProb"))
        bplvl = int(request.POST.get("bplvl"))
        model = load_model()
        predictions = model.predict_proba(np.array([sex, medInTime, age, timeSufDbt, avgDbtRate, type, otherProb, bplvl]).reshape(1, -1))
        comp_with_prob = list(zip(complications, predictions[0]))
        comp_with_prob.sort(key=(lambda val: val[1]), reverse = True)
        return render(request, "comp_detect/prediction.html", context = locals())
    else:
        return render(request, "comp_detect/treatment.html", context={'features': Feature.objects.all()})

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
