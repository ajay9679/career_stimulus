from django.shortcuts import render
from charity.models import Aboutus

def aboutus(request):
	about = Aboutus.objects.all()[:1]
	context = {'about':about}
	return render(request, 'charity/aboutus.html', context)









