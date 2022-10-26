from django.db import models

# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    text = models.TextField(blank=True)