from django.db import models

# Create your models here.
class Lista(models.Model):
	nazwa=models.CharField(max_length=40,default='lista zakupow')
	zawartosc=models.CharField(max_length=1000)