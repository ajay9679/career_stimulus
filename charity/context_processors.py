from django.conf import settings
from django.shortcuts import render, redirect
from charity.models import EmailPhone
from newsletter.models import NewsletterUser
from charity.forms import NewsletterForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

def display_email_phone(request):
    return {
        'email_phone': EmailPhone.objects.all().order_by('-id')[:1]
    }

def newsletter_form(request):
	if request.method == 'POST':
		form = NewsletterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			email_exist = NewsletterUser.objects.filter(email=email)
			if email_exist.exists():
				messages.warning(request, 'You are already subscribed.')
			else:
				create_email = NewsletterUser.objects.create(name=name, email=email)
				subject = 'Thanks for joining us'
				from_email = settings.EMAIL_HOST_USER
				to_email = [create_email.email]
				with open(str(settings.BASE_DIR) + '/charity/templates/charity/subscribe.txt') as f:
					newsletter_msg = f.read()
				html_template = render_to_string('charity/subscribe.html')
				text_format     =        strip_tags(html_template)
				message         =        EmailMultiAlternatives(subject=subject, body=text_format, from_email=from_email, to=to_email)
				message.attach_alternative(html_template, 'text/html')
				message.send()
				msg = True
				# messages.info(request, 'Thank you for subscribe.')				
	else:
		form = NewsletterForm()
	context = {'form':form}
	return context










