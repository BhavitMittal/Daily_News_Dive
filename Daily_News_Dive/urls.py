"""
URL configuration for Daily_News_Dive project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from django.contrib import admin
from django.urls import path
from . import views
from service import views as s

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/', s.Loginpage,name='login'),
    path('signup/', s.Signuppage,name='signup'),
    path('interest/', views.save_interests,name='interest'),
    path('science/', views.science , name='science'),
    path('technology/', views.technology , name='technology'),
    path('sports/', views.sports , name='sports'),
    path('business/', views.finance , name='finance'),
    path('health/', views.health , name='health'),
    path('entertainment/', views.entertainment , name='entertainment')
]
