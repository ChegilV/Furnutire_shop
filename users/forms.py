from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    # username = forms.CharField()
    # password = forms.CharField()

    # username = forms.CharField(
    #     label = 'Username',
    #     widget=forms.TextInput(attrs= {
    #         "autofocus": True, 
    #         'class': 'form-control',
    #         'placeholder': 'Enter your username'}))

    # password = forms.CharField(
    #     label = 'Password',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password", 
    #         'class': 'form-control',
    #         'placeholder': 'Enter your password',
    #         }),
    # )

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your first name',
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your last name',
    #         }
    #     )
    # )

    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your uesename',
    #         }
    #     )
    # )

    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your email',
    #         }
    #     )
    # )


    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter password',
    #         }
    #     )
    # )


    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Confirm the password',
    #         }
    #     )
    # )


class ProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    #     image = forms.ImageField(
    #         widget=forms.FileInput(attrs={'class': 'form-control mt-3'},
    #                                ), required=False
    #     )
        

    #     first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your first name',
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your last name',
    #         }
    #     )
    # )

    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your uesename',
    #         }
    #     )
    # )

    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": 'form-control',
    #             'placeholder': 'Enter your email',
    #         }
    #     )
    # )

