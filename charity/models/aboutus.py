from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Aboutus(models.Model):
	title 		= 		models.CharField(max_length=100, blank=False)
	body 		= 		RichTextUploadingField()
	created		=		models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'About Page'

	def __str__(self):
		return self.title






