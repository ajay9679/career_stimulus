from django.shortcuts import render
from charity.models import Contactus

def contactus(request):
	contact = Contactus.objects.all()[:1]
	context = {'contact':contact}
	return render(request, 'charity/contact.html', context)
