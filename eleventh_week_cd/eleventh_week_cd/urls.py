"""eleventh_week_cd URL Configuration

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

# url은 함수를 실행시켜 주는 것이다.

from django.contrib import admin
from django.urls import path
from doing.views import index, create, detail, delete, update   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:jss_id>', detail, name='detail'), # 우리는 html에서 url로 숫자값(id필드의 숫자)를 보냈다. int 라는 것은 숫자 형식이라는 것이고, : 뒤에 있는 것은 변수 이름이다. 이 변수 이름은 여기서 임의로 지어주는 것으로 나중에 views에서 함수의 인자로 사용되는 것이다.
    path('delete/<int:jss_id>', delete, name='delete'),
    path('update/<int:jss_id>', update, name='update'),
]
