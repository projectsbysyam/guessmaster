import re
from .models import Agent,Dealer
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.forms.widgets import EmailInput
from django.forms.widgets import TextInput


class LoginForm(UserCreationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control", "name": "username", "placeholder": "Username", "required": "required", "autocomplete": "off"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=TextInput(attrs={"class": "form-control", "name": "password1", "type": "password", "placeholder": "Password", "required": "required", "autocomplete": "off"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=TextInput(attrs={"class": "form-control", "name": "password2", "type": "password", "placeholder": "Confirm Password", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "name": "username", "placeholder": "Username", "required": "required", "autocomplete": "off"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "password1", "type": "password", "placeholder": "Password", "required": "required", "autocomplete": "off"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "password2", "type": "password", "placeholder": "Confirm Password", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

def phone_number_validation(value):
    if not re.compile(r"[0-9]\d{9}$").match(value):
        raise ValidationError("This is Not Valid Phone Number")


class AgentRegistration(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[phone_number_validation],
        widget=TextInput(attrs={"class": "form-control", "name": "phone_number", "placeholder": "Phone", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = Agent
        fields = ("agent_name", "phone_number")
        widgets = {
            "agent_name": TextInput(attrs={"class": "form-control", "name": "agent_name", "placeholder": "Name", "required": "required", "autocomplete": "off"}),
        }


class DealerRegistration(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[phone_number_validation],
        widget=TextInput(attrs={"class": "form-control", "name": "phone_number", "placeholder": "Phone", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = Dealer
        fields = ("dealer_name", "phone_number")
        widgets = {
            "dealer_name": TextInput(attrs={"class": "form-control", "name": "dealer_name", "placeholder": "Name", "required": "required", "autocomplete": "off"}),
        }