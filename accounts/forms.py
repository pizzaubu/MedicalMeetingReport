from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required=False)
    lastname = forms.CharField(max_length=50, required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'firstname', 'lastname')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อผู้ใช้'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'รหัสผ่าน'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

