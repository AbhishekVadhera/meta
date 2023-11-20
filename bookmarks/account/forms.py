from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='repeat-password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo', 'category']

    # def clean_password(self):
    #     cd = self.clean_password
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('password did not match')
    #     return cd['password2']

    # def clean_password(self):
    #     # cd = super().clean()
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #
    #     if password and password2 and password != password2:
    #         raise forms.ValidationError('password did not match')
    #     return password2
