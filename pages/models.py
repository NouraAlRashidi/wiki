from django.db import models
from django.urls import reverse

# Create your models here.
class Page (models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField ()
	last_update = models.DateTimeField (auto_now= True)

	# def get_absolute_url(self):
	# 	return "Title %s, Content %s, Last_Update %s"%(self.title, self.content, self.last_update)

	def get_absolute_url(self):
		return reverse ('page-detail', args=[str(self.id)])

	def __str__ (self):
		return self.title
