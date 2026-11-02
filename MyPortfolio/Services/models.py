from django.db import models

# Create your models here.

class services_model(models.Model):
    Service_title=models.CharField(max_length=70)
    Service_detail=models.TextField()
    