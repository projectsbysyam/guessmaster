import re
from .models import Agent,Dealer
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.widgets import EmailInput
from django.forms.widgets import TextInput


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


def phone_number_validation(value):
    if not re.compile(r"[0-9]\d{9}$").match(value):
        raise ValidationError("This is Not Valid Phone Number")


class AgentRegistration(forms.ModelForm):
    phone = forms.CharField(
        validators=[phone_number_validation],
        widget=TextInput(attrs={"class": "form-control", "name": "phone", "placeholder": "phone", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = Agent
        fields = ("agent_name","phone_number")
        widgets = {
            "agent_name": TextInput(attrs={"class": "form-control", "name": "agent_name", "placeholder": "Name", "required": "required", "autocomplete": "off"}),
            "phone_number": TextInput(attrs={"class": "form-control", "name": "phone_number", "placeholder": "Phone", "required": "required", "autocomplete": "off"}),
        }


class DealerRegistration(forms.ModelForm):
    phone = forms.CharField(
        validators=[phone_number_validation],
        widget=TextInput(attrs={"class": "form-control", "name": "phone", "placeholder": "phone", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = Dealer
        fields = ("dealer_name","phone_number")
        widgets = {
            "dealer_name": TextInput(attrs={"class": "form-control", "name": "dealer_name", "placeholder": "Name", "required": "required", "autocomplete": "off"}),
            "phone_number": TextInput(attrs={"class": "form-control", "name": "phone_number", "placeholder": "Phone", "required": "required", "autocomplete": "off"})
                    }