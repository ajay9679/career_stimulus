from django.shortcuts import render, HttpResponse, redirect
from charity.models import CharitableProjects, User
from charity.forms import DonateForm
from instamojo_wrapper import Instamojo
from career_stimulus.settings import PAYMENT_API_KEY, PAYMENT_API_AUTH_KEY
from charity.models import User

# API = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_API_AUTH_KEY, endpoint='https://test.instamojo.com/api/1.1/');

API = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_API_AUTH_KEY);

def verifypayment(request):
	payment_id = request.GET.get('payment_id')
	payment_request_id = request.GET.get('payment_request_id')
	response = API.payment_request_payment_status(payment_request_id, payment_id)
	status 			=			response['payment_request']['payment']['status']
	payment 		=			User.objects.get(payment_request_id=payment_request_id)
	if status != "Failed":
		payment.payment_id= 	response['payment_request']['payment']['payment_id']			
		payment.status= 		status
		payment.save()
		return render(request, 'charity/donate/thankyou.html', context={'payment' : payment})
	else:
		return redirect('home')

def donateview(request):
	if request.method == 'GET':
		return render(request, 'charity/donate/donate.html')
	else:
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		amount = request.POST.get('amount')
		
		# Create a new Payment Request
		response = API.payment_request_create(
    		amount=amount,
    		purpose='Testing Purpose',
    		send_email=True,
    		email=email,
    		redirect_url="http://localhost:8000/complete-payment"
    	)
		# # print(response['payment_request'])
		url 			= 			response['payment_request']['longurl']
		payment_request_id = 		response['payment_request']['id']
		user = User()
		user.name=name
		user.email=email
		user.phone=phone
		user.amount=amount
		user.payment_request_id=payment_request_id
		user.save()
		return redirect(url)








