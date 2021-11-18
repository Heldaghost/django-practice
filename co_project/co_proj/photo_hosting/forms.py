from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from photo_hosting.models import *


class EditUserForm(forms.ModelForm):
    usrname = forms.CharField(max_length=50)

    def __init__(self, user: User, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usrname'].initial = user.username
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    def __init__(self, user: User, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].initial = user.userprofile.description
        self.fields['avatar'].initial = user.userprofile.avatar
        self.fields['birth_date'].initial = user.userprofile.birth_date

    class Meta:
        model = UserProfile
        fields = ['description', 'avatar', 'birth_date']


class AddCollectionForm(forms.ModelForm):
    class Meta:
        model = Collections
        fields = ['title', 'description', 'avatar']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostsForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['collection'].queryset = Collections.objects.filter(posts__user_id=user_id).distinct()
        self.fields['collection'].empty_label = 'None'

    class Meta:
        model = Posts
        fields = ['title', 'content', 'photo', 'is_visible', 'collection', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 50:
    #         raise ValidationError('Длина превышает 200 символов')
    #     return title
