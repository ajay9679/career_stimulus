from django.contrib import admin
from newsletter.models import NewsletterUser

# Register your models here.

@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'date_added']
