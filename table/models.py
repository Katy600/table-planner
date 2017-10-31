from django.db import models
from django.utils import timezone

class GuestList(models.Model):
	first_name = models.CharField(max_length=200)
	second_name = models.CharField(max_length=200)
	gender = models.CharField(max_length = 200)

	def __str__(self):
		return self.first_name