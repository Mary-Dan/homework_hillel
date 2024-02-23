from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class MyRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Пароль повинен бути > 8 символів.")
        return password1


class MyLoginForm(AuthenticationForm):
    class Meta:
        model = None
        # Модель користувача, якщо вона вам потрібна для іншого поля, замініть на відповідне
        fields = ['username', 'password']

    # Додаткове поле для введення пароля
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

