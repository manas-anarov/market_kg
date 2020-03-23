from django.db import models


class OrderItem(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	telephone = models.CharField(max_length=400, default=0, blank=True)
	first_name = models.CharField(max_length=400, default=0, blank=True)
	last_name = models.CharField(max_length=400, default=0, blank=True)
	address = models.CharField(max_length=400, default=0, blank=True)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name