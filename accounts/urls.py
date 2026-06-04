"""
URL configuration for car_mart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path,include
from . import views 
from django.contrib.auth.views import LoginView

urlpatterns = [
   
   path('register/',views.RegisterView.as_view(),name='register'),
   path('login/',views.UserLoginView.as_view(),name='login'),
   path('edit/',views.ChangeUserForm.as_view(),name='edit_profile'),
   path('logout/',views.LoginView.as_view(next_page='home'),name='logout')
   
]
