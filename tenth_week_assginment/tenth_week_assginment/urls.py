"""tenth_week_assginment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import tenth_week_assginment_app.views

app_name  = 'tenth_week_assginment_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tenth_week_assginment_app.views.index.as_view(),name='index'),
    path('detail/<pk>',tenth_week_assginment_app.views.detail.as_view(),name="detail"),
    path('delete/<pk>',tenth_week_assginment_app.views.delete.as_view(),name="delete"),
    path('update/<pk>',tenth_week_assginment_app.views.update.as_view(),name="update"),
    path('create',tenth_week_assginment_app.views.create.as_view(),name='create'),
    path('result/',tenth_week_assginment_app.views.result,name='result'),
]

