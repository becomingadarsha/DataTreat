from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Message, Feature
from pydoc import locate
from django.forms.models import model_to_dict

def index(request):
    return render(request, "comp_detect/index.html")

def treatment(request):
    if(request.method == "POST"):
        features = request.POST.getlist("feature[]")
        feature_values = request.POST.getlist("feature_value[]")
        clean_data = {}
        for i, (feature_id, feature_value) in enumerate(zip(features, feature_values)):
            try:
                feature = Feature.objects.get(pk = int(float(feature_id)))
                value = locate(feature.dtype)(feature_value)
                clean_data[i] = {feature.name: value}
            except (Feature.DoesNotExist, ValueError) as e:
                pass
        return JsonResponse(clean_data, safe=False)
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
