from django.db import models

class Caretaker(models.Model):
	name = models.CharField(max_length=30, default="Visitor")
	active = models.BooleanField(default=False)
	channel = models.CharField(max_length=30)

