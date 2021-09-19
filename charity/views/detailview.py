from django.shortcuts import render, HttpResponse, redirect
from charity.models import CharitableProjects, ProjectsImages

def detailview(request, slug):
	charity_detail = CharitableProjects.objects.get(slug=slug)
	carousel_images = ProjectsImages.objects.filter(project=charity_detail.id)
	print(carousel_images)
	context = {
		'charity_detail' : charity_detail,
		'carousel_images' : carousel_images
	}
	return render(request, 'charity/detail.html',  context)








