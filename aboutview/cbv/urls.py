from django.urls import path

from . import views

app_name = 'cbv'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id/vote/', views.vote, name='vote')
]

# 한 가지 html에 여러가지 views가 올 수 있다