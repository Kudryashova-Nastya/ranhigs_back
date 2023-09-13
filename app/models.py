from django.contrib.auth.models import User
from django.db import models


class StatusSession(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    teamCount = models.PositiveSmallIntegerField()
    link = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datetimeStart = models.DateTimeField(auto_now_add=True)
    statusID = models.ForeignKey(StatusSession, on_delete=models.PROTECT, related_name='session')
    timer = models.TimeField()
    timerIsActive = models.BooleanField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    pincode = models.PositiveSmallIntegerField()
    userCount = models.PositiveSmallIntegerField()
    sessionID = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='team')
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
