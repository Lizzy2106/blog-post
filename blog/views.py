from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
# from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import *
from .forms import *

from django.contrib import messages
from django.conf import settings

# Create your views here.

def home(request):
	posts = Post.objects.all().order_by('-created_at')
	paginator = Paginator(posts, 4)

	page_number = request.GET.get('page')

	page_obj    = paginator.get_page(page_number)
	context={
		'posts':page_obj,
	}
	return render(request, 'index.html', context)

def new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			post = form.cleaned_data.get('title')
			messages.success(request, 'Votre article a été publié: ' + post)

			return redirect('home')
	form = PostForm()
	context={
		'form':form,
	}
	return render(request, 'new.html', context)

def post(request, pk):
	post=Post.objects.get(id=pk)
	context={
		'post':post,
	}
	return render(request, 'post.html', context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Create the email and send the message
			email = settings.EMAIL_HOST_USER
			subject = f"BlogPost Contact Form:  {form['name'].value()}"
			body = {
				'headers' :f"From: noreply.{email}",
				'content': f"You have received a new message from your website contact form.\n. Here are the details:",
				'message': {
					'Name': f"Name: {form['name'].value()}",
					'Email': f"Email: {form['email'].value()}",
					'Phone': f"Phone: {form['phone'].value()}",
					'Message': f"Message: {form['message'].value()}",

				},
				'footer': f"Reply-To: {form['email'].value()}",
			}
			body['message'] = "\n".join(body['message'].values())
			message = "\n\n".join(body.values())
			try:
				send_mail(
					subject,
					message,
					f"noreply.{email}",
					[email,],
					fail_silently=False
				)
			except BadHeaderError:
				messages.info(request, 'Invalid header found.')
			messages.success(request, 'Your email has been sent.')
			return redirect('home')
	form = ContactForm()
	context={
		'form':form,
	}
	return render(request, 'contact.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Create the email and send the message
			email = settings.EMAIL_HOST_USER
			subject = f"BlogPost Contact Form:  {form['name'].value()}"
			body = {
				'headers' :f"From: noreply.{email}",
				'content': f"You have received a new message from your website contact form.\n. Here are the details:",
				'message': {
					'Name': f"Name: {form['name'].value()}",
					'Email': f"Email: {form['email'].value()}",
					'Phone': f"Phone: {form['phone'].value()}",
					'Message': f"Message: {form['message'].value()}",

				},
				'footer': f"Reply-To: {form['email'].value()}",
			}
			body['message'] = "\n".join(body['message'].values())
			message = "\n\n".join(body.values())


			c = {
				'message':{
					'name':form['name'].value(),
					'email':form['email'].value(),
					'phone':form['phone'].value(),
					'subject':form['subject'].value(),
					'message':form['message'].value(),

				}
			}
			html_content = get_template('mail.html').render(c)
			msg = EmailMultiAlternatives(
					subject,
					message,
					f"noreply.{email}",
					[email,]
			)
			msg.attach_alternative(html_content, "text/html")
			try:
				msg.send()
			except BadHeaderError:
				messages.info(request, 'Invalid header found.')
			messages.success(request, 'Your email has been sent.')
			return redirect('home')
	form = ContactForm()
	context={
		'form':form,
	}
	return render(request, 'contact.html', context)

def about(request):
	context={}
	return render(request, 'about.html', context)
