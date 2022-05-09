from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Employee(models.Model):
	f_name = models.CharField(max_length=255)
	l_name = models.CharField(max_length=255)
	salary = models.IntegerField(default=0)
	bonus = models.IntegerField(default=0)
	img_url = models.CharField(max_length=2083)
	phone_no = models.IntegerField()
	role = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	location = models.CharField(max_length=255)
	hr_date = models.DateTimeField(default=timezone.now)
	r = models.IntegerField(default=0)