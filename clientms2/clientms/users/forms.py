from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'department', 'employee_cell_phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'department', 'employee_cell_phone')

class CustomPasswordResetForm(PasswordResetForm):

    class Meta:
        model = CustomUser
        fields = ('email')