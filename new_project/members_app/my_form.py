from django import forms
# створюємо три окреми форми: сторінка вводу,
# сторінка відображення користувацького вводу
# та додаткову сторінку
class UserInputForm(forms.Form):
    user_input = forms.CharField(label='User Input')


class DisplayForm(forms.Form):
    display = forms.CharField(label='Display Input')


class SessionForm(forms.Form):
    value = forms.CharField(label='Session Value')
