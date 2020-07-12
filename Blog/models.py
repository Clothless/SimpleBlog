from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class post(models.Model):
	title = models.CharField(max_length=255)
	auther = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.auther)


	def get_absolute_url(self):
		return reverse('home')