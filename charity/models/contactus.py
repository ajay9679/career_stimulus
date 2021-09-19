from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Contactus(models.Model):
	body 		= 		RichTextUploadingField()
	created		=		models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Contact Page'

	def __str__(self):
		return self.body