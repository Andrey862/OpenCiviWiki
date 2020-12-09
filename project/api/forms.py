
from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User
from models import Account

class UpdatePassword(forms.ModelForm):
    """
    Form for updating User Password
    """
    class Meta:
        model = User
        fields = ['password', 'verify']

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    verify = forms.CharField(
        label="Password Verify",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password Verify',
                'required': 'True',
            }
        ),
        help_text="Please retype your password."
    )

    def clean(self):
        """
        Verifies that the passwords match
        """
        clean_data = super(UpdatePassword, self).clean()
        if 'password' in clean_data and 'verify' in clean_data:
            if clean_data['password'] != clean_data['verify']:
                raise forms.ValidationError("Passwords don't match.")
        else:
            raise forms.ValidationError("Both password fields need to be filled out.")
        return clean_data

class UpdateAccount(forms.ModelForm):
    """
    Form for updating Account data
    """
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'about_me', 'profile_image']

    first_name = forms.CharField(label='First Name', max_length=63, required=False)
    last_name = forms.CharField(label='Last Name', max_length=63, required=False)
    about_me = forms.CharField(label='About Me', max_length=511, required=False)
    profile_image = forms.ImageField(required=False)
