from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View, TemplateResponseMixin

class RegisterView(TemplateResponseMixin, View):
	template_name = 'charity/register/register.html'
	
	
	def get(self, request):
		return self.render_to_response({})






