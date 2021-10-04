from django.shortcuts import render, redirect
from charity.writeToUsForm import writeToUsForm
from charity.models import writeToUsModel

def WriteWithUsView(request):
    if(request.method == 'GET'):
    	form = writeToUsForm()
    	return render(request, 'charity/write.html', {'form':form})
    else:
    	form = writeToUsForm(request.POST)
    	if form.is_valid():
    		name = form.cleaned_data.get('name')
    		email = form.cleaned_data.get('email')
    		phone = form.cleaned_data.get('phone')
    		subject = form.cleaned_data.get('subject')
    		feedback = form.cleaned_data.get('feedback')
    		writetous = writeToUsModel()
    		writetous.name = name
    		writetous.email = email
    		writetous.phone = phone
    		writetous.subject = subject
    		writetous.feedback = feedback
    		writetous.save()
    		return redirect('charity:home')
    	else:
    		return redirect('charity:home')

