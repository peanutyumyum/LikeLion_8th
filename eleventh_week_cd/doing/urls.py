from django.urls import path
from .views import index, create, detail, delete, update,create_comment, delete_comment


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:jss_id>', detail, name='detail'), # 우리는 html에서 url로 숫자값(id필드의 숫자)를 보냈다. int 라는 것은 숫자 형식이라는 것이고, : 뒤에 있는 것은 변수 이름이다. 이 변수 이름은 여기서 임의로 지어주는 것으로 나중에 views에서 함수의 인자로 사용되는 것이다.
    path('delete/<int:jss_id>', delete, name='delete'),
    path('update/<int:jss_id>', update, name='update'),
    path('create_comment/<int:jss_id>', create_comment, name='create_comment'),
    path('delete_comment/<int:jss_id>/<int:comment_id>', delete_comment, name='delete_comment')
]