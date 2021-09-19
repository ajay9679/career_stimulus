from django.shortcuts import render

def gallery(request):
	return render(request, 'charity/gallery.html')