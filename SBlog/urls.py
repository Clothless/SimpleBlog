from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('authen/', include('django.contrib.auth.urls')),
    path('authen/', include('authen.urls')),
]
