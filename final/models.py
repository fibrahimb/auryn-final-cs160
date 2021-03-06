from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Activity(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    date = models.DateField()
    active_d = models.BooleanField(default=False)
    active_q = models.BooleanField(default=False)

    @classmethod
    def create(cls, question, date):
        created = cls(question=question, date=date)
        return created

class QA(models.Model):
    youranswer = models.CharField(max_length = 3000)

    @classmethod
    def create(cls, youranswer):
        created = cls(youranswer=youranswer)
        return created


class Driver(models.Model):
    bio = models.CharField(max_length=1000)

    @classmethod
    def create(cls, bio):
        created = cls(bio=bio)
        return created

class Answers(models.Model):
    q_id = models.ForeignKey('Activity', on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()

    @classmethod
    def create(cls, answer):
        created = cls(answer=answer)
        return created

class Files(models.Model):
    q_id = models.ForeignKey('Activity', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField()

class Map_Q(models.Model):
    #q_id = models.ForeignKey('Activity', on_delete=models.CASCADE)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    @classmethod
    def create(cls, lat, lon, date):
        created = cls(lat=lat, lon=lon, timestamp=date)
        return created
