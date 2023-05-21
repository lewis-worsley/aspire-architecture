from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


class RegisterStaffUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=90,
        help_text="Must register with company email domain '@aspire.com'",
        validators=[
            RegexValidator(
                regex='^^\w+@aspire\.com$',
                message='Invalid email address. Please use the @aspire.com domain',
                code='invalid email address'
            ),
        ])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
