from django import forms
from accounts.models import User

class AdminLoginForms(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.Input(attrs={"class":"form-control","placeholder":"ชื่อผู้ใช้งาน" }),
        label="ชื่อผู้ใช้งาน"
    )

    password = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(attrs={"class":"form-control","placeholder":"รหัสผ่าน" }),
        label="รหัสผ่าน"
    )

    class Meta:
        model = User
        fields = ['username','password']
