"""todopro2 URL Configuration

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
from todoapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',views.ToDoView,name='main'),
    path('add',views.homepage,name='add'),
    path('data/<id>',views.fetchingdata,name='data'),
    path('update/<id>',views.update,name='update'),
    path('updating/<id>',views.updating,name='updating'),
    path('delete/<id>',views.delete,name='delete')
]
