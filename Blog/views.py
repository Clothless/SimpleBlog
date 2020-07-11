from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy




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


class EditPost(UpdateView):
	model = post
	template_name = 'edit.html'
	fields = '__all__'


class DeletePost(DeleteView):
	model = post
	template_name = 'delete.html'
	success_url = reverse_lazy('home')