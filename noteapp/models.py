from django.db import models

# Create your models here.
class Notes(models.Model):
    name_id = models.IntegerField()
    name = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
