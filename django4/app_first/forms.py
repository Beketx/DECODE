from django.forms import ModelForm
from app_first.models import Post
from django.contrib.auth.models import User
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'views', 'cover']

# class TagForm(forms.Form):
#     name = forms.CharField(max_length=100)

class LoginForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'Login'
    #     self.fields['password'].label = 'Password'

    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
            'username': None
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }