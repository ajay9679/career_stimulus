from django.contrib import admin
from charity.models import CharitableProjects, User, EmailPhone, Aboutus, ProjectsImages, Contactus
from django.utils.html import format_html
from instamojo_wrapper import Instamojo
from career_stimulus.settings import PAYMENT_API_KEY, PAYMENT_API_AUTH_KEY

API = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_API_AUTH_KEY)

# Register your models here.

class ProjectsImageModel(admin.StackedInline):
	model = ProjectsImages

@admin.register(CharitableProjects)
class CharitableProjectsAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'get_image', 'active', 'created']
	list_display_links = ('title',)
	list_editable = ('active',)
	raw_id_fields = ('author',)
	prepopulated_fields = {'slug': ('title',)}
	list_per_page = 2
	inlines = [ProjectsImageModel]

	# def get_body(self, obj):
	# 	return format_html(f'<span title="{obj.body}">{obj.body[0:15]}....<span>')

	def get_image(self, obj):
		return format_html(f'''<img height="70" width="150" src='{obj.image.url}'>''')

	get_image.short_description = 'image'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'amount', 'payment_request_id', 'get_status', 'payment_id', 'created']
	readonly_fields = (
		'name', 'email', 'phone', 'amount', 'payment_request_id', 'payment_id', 'created',
	)

	def get_status(self, obj):
		response = API.payment_request_status(obj.payment_request_id)
		obj.paymentDetails=response
		if obj.status != "Failed":
			return True
		else:
			return False

	get_status.short_description = 'status'
	get_status.boolean = True

@admin.register(EmailPhone)
class EmailPhoneAdmin(admin.ModelAdmin):
	list_display = ['email', 'phone']

@admin.register(Aboutus)
class AboutUsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']

@admin.register(Contactus)
class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['created']



