from django.db import models
from django.contrib.auth.models import User


class post(models.Model):
	title = models.CharField(max_length=255)
	auther = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()

	def __str__(self):
		return self.title + ' | ' + self.auther