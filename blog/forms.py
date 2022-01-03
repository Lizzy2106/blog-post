from django import forms
from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
	class Meta(object):
		model = Post
		fields = '__all__'
		exclude = ['created_at']
			
class ContactForm(forms.Form):
	"""docstring for Meta"""
	subject = forms.CharField(max_length=100)
	name    = forms.CharField(max_length=100)
	email   = forms.CharField(max_length=100)
	phone   = forms.CharField(max_length=100)
	message = forms.CharField(max_length=100)
	class Meta(object):
		fields = [
			'subject',
			'name',
			'email',
			'phone',
			'message',
		]
			
		
