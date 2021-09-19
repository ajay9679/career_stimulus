# from django.db import models
# from charity.models import User

# class Payment(models.Model):
# 	user 				=			models.ForeignKey(User, null=True, on_delete=models.CASCADE)
# 	payment_request_id	=			models.CharField(max_length=300, null=False, unique=True)
# 	payment_id			=			models.CharField(max_length=300, null=True, unique=False)
# 	status 				=			models.CharField(max_length=300, default="Failed")
# 	created				=			models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.payment_request_id