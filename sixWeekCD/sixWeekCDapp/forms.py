from django import forms

class crateForm(forms.Form):
    RECOMMEND_CHOICES = (
        ('1','★☆☆☆☆'),
        ('2','★★☆☆☆'),
        ('3','★★★☆☆'),
        ('4','★★★★☆'),
        ('5','★★★★★'),
    )
    recommend = forms.ChoiceField(choices=RECOMMEND_CHOICES)

    photo = forms.ImageField(label="photo")