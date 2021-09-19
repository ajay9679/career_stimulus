from django import forms
from charity.models import User, CharitableProjects
from newsletter.models import NewsletterUser

class DonateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'name',
			'email',
			'phone',
			'amount',
		]

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if phone is None:
			raise forms.ValidationError("This value cannot be empty")
		return phone	

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = NewsletterUser
		fields = [
			'name', 'email',
		]
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter Email'}),
        }





