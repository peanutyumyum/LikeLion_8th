from django import forms

class crateForm(forms.Form):
    photo = forms.ImageField(label="photo")