from django.contrib.auth import get_user_model # importing the get_user_model function to get the current user model used in the project
from django.contrib.auth.forms import UserCreationForm # importing the standard user creation form UserCreationForm
from django import forms # importing the forms module from Django to create your own form fields

User = get_user_model() # get the user model that is defined for the current project

class UserCreationForm(UserCreationForm): # to override user
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}) # setting up the widget as an email field
    )
    class Meta(UserCreationForm.Meta): # the meta class allows you to set additional settings for the form
        model = User
        fields = ("username", "email")