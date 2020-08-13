from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content', )

    def __init__(self, *args, **kwargs): # class 안에 있는 함수는 무조건 self를 첫번째 인자로 가짐
        super().__init__(*args, **kwargs) # super는 부모클래스에 있는 것들을 가져와 쓸 수 있음(즉 부모 클래스에 있는 __init__을 가져와서 쓸 수 있음 자동 생성하는 필드, 모델, 폼들의 속성이 들어있음)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class' : 'jss_title', # title 이라는 form에 class의 이름을 생성해줌
            'placeholder' : '제목'
        })
