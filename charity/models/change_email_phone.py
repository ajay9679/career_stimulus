from django.db import models

class EmailPhone(models.Model):
	email = models.EmailField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.email





