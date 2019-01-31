from django.db import models
from django.core.validators import RegexValidator

class Feature(models.Model):
    name = models.CharField(max_length = 200)
    unit = models.CharField(max_length = 50)
    dtype = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length = 200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length = 17)
    message = models.TextField()

    def __str__(self):
        return self.name
