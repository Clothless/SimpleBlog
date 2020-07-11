from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post



#def home(requests):
# 	return render(requests, "index.html", {})


class HomeView(ListView):
	model = post
	template_name = "index.html"


class ArticleView(DetailView):
	model = post
	template_name = "article.html"