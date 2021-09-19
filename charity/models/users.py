from django.db import models

class User(models.Model):
	name 				= 			models.CharField(max_length=50)
	email				=			models.CharField(max_length=100)
	phone				=			models.CharField(max_length=10)
	amount 				= 			models.PositiveIntegerField(default=0, blank=False)
	active              =           models.BooleanField(default=True)
	payment_request_id	=			models.CharField(max_length=255, null=False, unique=True)
	payment_id			=			models.CharField(max_length=300, null=True, unique=False)
	status 				=			models.CharField(max_length=300, default="Failed")
	created				=			models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Payment Info'





