"""
URL configuration for officemanagement project.

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
from django.urls import include
from employee import views as view

urlpatterns = [
   path('' , view.index , name='index'),
   path('add_employee/' , view.add_employee , name='add_employee'),
   path('remove_employee/' , view.remove_employee , name='remove_employee'),
   path('edit_employee/' , view.edit_employee , name='edit_employee'),



]
