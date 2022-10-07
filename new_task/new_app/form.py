from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    usertype = forms.ChoiceField(choices=[("Patient", "Patient"), ("Doctor", "Doctor")])
    profile_picture = forms.ImageField()
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", 'first_name', 'last_name',)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.usertype = self.cleaned_data['usertype']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        user.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            user.save()
        return user