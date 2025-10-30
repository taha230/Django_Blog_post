from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.TextInput()
    is_enable = forms.BooleanField()
    publish_date = forms.DateField()