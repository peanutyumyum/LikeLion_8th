from django.urls import path

from . import views

app_name = 'fbv'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id/vote/', views.vote, name='vote')
]

# 한 가지 html에 여러가지 views가 올 수 있다