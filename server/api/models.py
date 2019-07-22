from __future__ import unicode_literals
from django.db import models

class Session(models.Model):
	session_name = models.CharField(max_length=200, unique=True)
	color = models.CharField(max_length = 10, default="white")

	def __str__(self):
		return self.session_name

class Stone(models.Model):
	room = models.ForeignKey(Session, related_name='stone_session', on_delete=models.CASCADE, null=True, blank=True)
	color = models.CharField(max_length = 10, default="white")
	x1 = models.CharField(max_length = 10)
	y1 = models.IntegerField()
	x2 = models.CharField(max_length = 10, blank=True)
	y2 = models.IntegerField(blank=True)

	def __str__(self):
		return self.color

class ResultOmok(models.Model):
	room = models.IntegerField()
	color = models.CharField(max_length=10)
	x = models.CharField(max_length = 10)
	y = models.IntegerField()

	def __str__(self):
		return self.color

class UserSession(models.Model):
    user_id = models.CharField(default="",max_length=200,primary_key=True)
    user_name = models.CharField(default="",max_length=50)

# Create your models here.
