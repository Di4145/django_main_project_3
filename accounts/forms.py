from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class UserRegistrationForm(forms.ModelForm):
#     password1 = forms.CharField(widget=forms.PasswordInput, label='password')
#     password2 = forms.CharField(widget=forms.PasswordInput, label='repeat password')
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'email']
#
#
#     def clean_password2(self):
#         passwords = self.cleaned_data
#         password1 = passwords['password1']
#         password2 = passwords['password2']
#         if password1 != password2:
#             raise forms.ValidationError('Password dont match')
#         return passwords['password2']
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой e-mail уже существует ')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'data']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name']
