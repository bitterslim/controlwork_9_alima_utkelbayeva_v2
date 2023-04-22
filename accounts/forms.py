from django import forms
from django.contrib.auth import get_user_model


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    password_confirm = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_confirm']
        labels = {
            'username': '',
            'email': ''
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Wrong Password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя пользователя'})
    )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'})
    )
