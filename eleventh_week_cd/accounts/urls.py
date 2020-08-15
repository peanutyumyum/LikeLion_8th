from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"), # as_view 를 사용하는 이유는 def가 아니라 clss 이기 때문에 instance를 생성해야 실행 할 수 있음(ClassBaseView사용하기)
    path('logout', LogoutView.as_view(), name="logout"),
]