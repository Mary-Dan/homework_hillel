from django import forms
from .models import Consultation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import File


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['doctor', 'date', 'duration', 'description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control datetime-input', 'placeholder': 'Select date and time'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration in minutes'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description (optional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']