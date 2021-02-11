from django.db import models

# Create your models here.
class ClientInfo(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)