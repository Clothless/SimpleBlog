from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import post




class HomeView(ListView):
	model = post
	template_name = "index.html"


class ArticleView(DetailView):
	model = post
	template_name = "article.html"


class AddPost(CreateView):
	model = post
	template_name = 'add.html'
	fields = '__all__'