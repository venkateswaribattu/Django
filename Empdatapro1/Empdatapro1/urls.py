"""Empdatapro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Empdataapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.emplayeedataView),
    path('fetch_all',views.fetchingalldata),
    path('',views.mainPage),
    path('mainPage',views.mainPage,name='mainPage'),
    path('Hyd',views.hyderabaddata,name='Hyd'),
    path('Bang',views.bangdata,name='Bang'),
    path('Che',views.chedata,name='Che'),
    path('Pune',views.punedata,name='Pune')

]
