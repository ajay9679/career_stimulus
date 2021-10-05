from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from charity.models import CharitableProjects

def ourWork(request):
	projects = CharitableProjects.objects.filter(active=True).select_related('author').order_by('-created')
	page = request.GET.get('page')
	if page is None or page == '':
		page = 1
	paginator = Paginator(projects, 20)
	page_obj = paginator.get_page(page)
	context = {'page_object':page_obj}
	return render(request, 'charity/ourWork.html', context)
