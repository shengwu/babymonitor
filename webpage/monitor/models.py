from django.db import models

"""
class Caretaker(models.Model):
	#name = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=11)
	password = models.CharField(max_length=30)
	primary = models.BooleanField(default=False)
	access = models.BooleanField(default=False)	
"""

class Baby(models.Model):
	name = models.CharField(max_length=30, default="Baby")

class Cry(models.Model):
	baby = models.ForeignKey(Baby)
	time = models.DateTimeField(auto_now_add=True)
	length = models.FloatField()
	volume = models.FloatField()

class Sleep(models.Model):
	baby = models.ForeignKey(Baby)
	time = models.DateTimeField()
	length = models.FloatField() 
	interruptions = models.IntegerField(default=0)

class DataPoint(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()
    humidity = models.FloatField()
