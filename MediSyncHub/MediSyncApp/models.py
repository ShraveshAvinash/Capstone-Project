from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(models.Model):
    phone_no = PhoneNumberField()
    address = models.CharField(max_length=255)


