from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.Form):
  username = forms.CharField(label="Username")
  password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))


# special form so that we can jam in the
# autocomplete attribute for the password input field
class AuthForm(AuthenticationForm):
  password = forms.CharField(
    label=("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete":"new-password"}),
  )