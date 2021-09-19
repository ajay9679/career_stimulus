from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class CharitableProjects(models.Model):
	title 		= 		models.CharField(max_length=100)
	author 		= 		models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	slug 		= 		models.SlugField(max_length=200)
	body 		= 		RichTextUploadingField()
	active      =       models.BooleanField(default=True)
	image       =       models.ImageField(null=True, blank=True, upload_to='uploads/images', default='D:/django/career_stimulus/charity/static/images/no_image.png')
	created		=		models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Charitable Project'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('charity:detailview', args=[self.slug])

class ProjectsImages(models.Model):
    project      =       models.ForeignKey(CharitableProjects, on_delete=models.CASCADE)
    image        =       models.ImageField(upload_to='uploads/images', blank=True)

    class Meta:
        verbose_name_plural = 'Project Image'




