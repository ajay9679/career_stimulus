from django.db import models

class writeToUsModel(models.Model):
	name 		= 		models.CharField(max_length=100)
	email 		= 		models.CharField(max_length=100)
	phone 		= 		models.CharField(max_length=10)
	subject 	= 		models.CharField(max_length=100)
	feedback 	= 		models.TextField(max_length=300)
	created		=		models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name