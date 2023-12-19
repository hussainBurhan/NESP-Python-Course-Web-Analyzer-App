"""
URL configuration for WebAnalyzer project.

The `urlpatterns` list routes URLs to views. For more information, please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import necessary modules
from django.contrib import admin
from django.urls import path
from . import views

# Define URL patterns for the WebAnalyzer app
urlpatterns = [
    # Admin URL for Django admin interface
    path('admin/', admin.site.urls),
    
    # URL for the home page, linked to the 'home' view function
    path('', views.home, name='home'),
    
    # URL for processing the form and displaying results, linked to the 'result' view function
    path('result', views.result, name='result'),
]
