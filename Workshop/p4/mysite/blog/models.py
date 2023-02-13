from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=200)
	des = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(default=datetime.now())
