from django.db import models

# Create your models here.
class Registro(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
