from django.db import models

# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	title      = models.CharField(max_length=200, null=True)
	resum      = models.CharField(max_length=200, null=True)
	content    = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title