from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('new', new, name='new'),
	path('post/<str:pk>/', post, name='post'),
	path('contact', contact, name='contact'),
	path('about', about, name='about'),
]
