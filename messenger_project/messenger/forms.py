from django import forms
from .models import Chat, Message


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class AddUserForm(forms.Form):
    username = forms.CharField(max_length=30)


class EditMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class DeleteMessageForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class DeleteUserForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)