from django.db import models


class Baby(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    max_vol = models.FloatField(default=10)
    min_temp = models.FloatField(default=5)
    max_temp = models.FloatField(default=20)

class Sleep(models.Model):
	baby = models.ForeignKey(Baby)
	time = models.DateTimeField()
	length = models.FloatField() 
	interruptions = models.IntegerField(default=0)

class Cry(models.Model):
    sleep = models.ForeignKey(Sleep)
    baby = models.ForeignKey(Baby)
    time = models.DateTimeField(auto_now_add=True)
    length = models.FloatField()
    volume = models.FloatField()

class DataPoint(models.Model):
    sleep = models.ForeignKey(Sleep)
    baby = models.ForeignKey(Baby)
    time = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()
    humidity = models.FloatField()
