from django.db import models
from django.utils import timezone

class GuestList(models.Model):
	first_name = models.CharField(max_length=40)
	spouse = models.CharField(max_length = 40)

	def __str__(self):
		return self.first_name