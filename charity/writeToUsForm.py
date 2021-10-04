from django import forms
from django.contrib.auth.models import User
from charity.models import writeToUsModel

class writeToUsForm(forms.ModelForm):
	class Meta:
		model = writeToUsModel
		fields = ['name', 'email', 'phone', 'subject', 'feedback']