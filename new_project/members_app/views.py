from django.shortcuts import render, redirect
from .my_form import UserInputForm, SessionForm


def input_page(request):
    """
    Представлення для сторінки вводу.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data.get('user_input')
            if user_input is not None:
                return render(request, 'members_app/display_input.html', {'user_input': user_input})
    else:
        form = UserInputForm()
    return render(request, 'members_app/input_page.html', {'form': form})


def display_input(request):
    """
    Представлення для відображення введеного користувачем тексту.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """

    user_input = request.session.get('user_input', None)
    if user_input is None:
        return redirect('input_page')

    return render(request, 'members_app/display_input.html', {'user_input': user_input})


def session_page(request):
    """
    Представлення для сторінки роботи з сесіями.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('value')
            if value is not None:
                request.session['value'] = value
    else:
        form = SessionForm()

    session_value = request.session.get('value', None)
    return render(request, 'members_app/session_page.html', {'form': form, 'session_value': session_value})
