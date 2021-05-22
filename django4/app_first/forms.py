from django.forms import ModelForm
from app_first.models import Post
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'views', 'cover']

# class TagForm(forms.Form):
#     name = forms.CharField(max_length=100)

class LoginForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise ValidationError(f'User not found in system')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise ValidationError('Not correct password')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
            'username': None,
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    phone = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}
                            ))
    address = forms.CharField(required=False,
                              widget=forms.TextInput(
                                  attrs={'class':'form-control'}
                              ))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control'}
                             ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['email'].label = 'Почта'
        self.fields['confirm_password'].label = 'Пароль 2'

    def clean_email(self):
        email = self.cleaned_data['email'] #askar@gmail.com
        domain = email.split('.')[-1] #com
        if domain in ['ru', 'net']:
            raise forms.ValidationError(f'This domains is not acceptable, try com variant')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This user already registered')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'This username is taken')
        return username

    # def clean(self):
    #     password = self.cleaned_data['password'] #123
    #     confirm_password = self.cleaned_data['confirm_password'] #124
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(f'Password is not same')
    #     return self.cleaned_data

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'address',
            'phone',
            'email'
        ]

        help_texts = {
            'username': None,
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }