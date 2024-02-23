from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class MyUserCreationForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        errors = password_validation.validate_password(password1)
        if errors:
            raise ValidationError(errors)
        return password1

