from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[("DOC", "Doctor"), ("PAT", "Patient")])
    profile_picture = forms.ImageField()
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", 'first_name', 'last_name', 'user_type', 'profile_picture', 'address']

