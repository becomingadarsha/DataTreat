from django.urls import path

from . import views

app_name = "comp_detect"
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('message/', views.save_message, name="message"),
    path('treatment/', views.treatment, name="treatment"),
]
