from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']