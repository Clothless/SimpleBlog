from django.urls import path
#from . import views
from .views import HomeView, ArticleView, AddPost, EditPost, DeletePost

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('AddPost', AddPost.as_view(), name="add"),
    path('article/edit/<int:pk>', EditPost.as_view(), name="edit"),
    path('article/delete/<int:pk>', DeletePost.as_view(), name="delete"),
    
]
