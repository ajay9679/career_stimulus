from django.shortcuts import render, redirect, get_object_or_404
from charity.models import CharitableProjects, ProjectsImages
from django.contrib import messages
from newsletter.models import NewsletterUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
	projects = CharitableProjects.objects.filter(active=True).select_related('author').order_by('-created')
	recent_image = CharitableProjects.objects.filter(active=True).select_related('author').order_by('-created')[0]
	current_project = recent_image
	carousel_images = ProjectsImages.objects.filter(project=current_project.id)
	page = request.GET.get('page')
	if page is None or page == '':
		page = 1
	paginator = Paginator(projects, 20)
	page_obj = paginator.get_page(page)
	context = {'page_object':page_obj, 'carousel_images':carousel_images, 'current_project':current_project, 'recent_image':recent_image,}
	return render(request, 'charity/index.html', context)








