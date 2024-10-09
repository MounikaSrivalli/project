# demoproject/urls.py

from django import views
from django.contrib import admin
from django.urls import path, include
from .views import getHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('carreviews.urls')),  # Include app URLs
    path('',getHome,name="home")
]
