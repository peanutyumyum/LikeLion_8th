"""ten_week_cbv URL Configuration

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
import cbv.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cbv.views.index.as_view(), name='index'),
    path('detail/<pk>', cbv.views.detail.as_view(), name='detail'),
    path('update/<pk>', cbv.views.update.as_view(), name='update'),
    path('delete/<pk>', cbv.views.delete.as_view(), name='delete'),
    path('create/', cbv.views.create.as_view(), name='create'),
    path('result/', cbv.views.result, name='result'),
]