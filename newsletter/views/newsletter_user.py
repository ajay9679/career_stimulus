from django.shortcuts import render

def newsletter_form(request):
	print('hello')
	if request.method == 'POST':
		name = request.POST.get('name')
		print(name)

















		


