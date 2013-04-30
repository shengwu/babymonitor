from django.db import models

class Caretaker(models.Model):
    name = models.CharField(max_length=30, default="Visitor")
    active = models.BooleanField(default=False)
    channel = models.CharField(max_length=30)

class Cry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    length = models.FloatField()
    volume = models.FloatField()
