from django.contrib import admin
from django.urls import path, include
from . import views
from charity.views import index
from charity.views import gallery
from charity.views import aboutus
from charity.views import contactus
from charity.views import RegisterView, detailview, donate, WriteWithUsView, ourWork

app_name = 'charity'

urlpatterns = [
    path('', index.index, name='home'),
    
    path('gallery/', gallery.gallery, name='gallery'),
    path('about/us/', aboutus.aboutus, name='aboutus'),
    path('contact/us/', contactus.contactus, name='contactus'),
    path('projects/<slug:slug>/', detailview.detailview, name='detailview'),
    path('donate/', donate.donateview, name='donateview'),
    path('complete-payment/', donate.verifypayment, name='verifypaymentview'),
    path('register/', RegisterView.as_view(), name='register'),
    path('write-with-us/', WriteWithUsView, name='write-with-us'),

    path('our-works/', ourWork, name='ourworks'),
]