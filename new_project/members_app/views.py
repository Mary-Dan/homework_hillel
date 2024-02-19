from django.shortcuts import render
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
            user_input = form.cleaned_data['user_input']
            return render(request, 'members_app/display_input.html', {'user_input': user_input})
    else:
        form = UserInputForm()
    return render(request, 'members_app/input_page.html', {'form': form})

def display_input(request):
    """
    Представлення для сторінки відображення користувацького вводу.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            return render(request, 'members_app/display_input.html', {'user_input': user_input})
    else:
        form = UserInputForm()
    return render(request, 'members_app/input_page.html', {'form': form})

def session_page(request):
    """
    Представлення для сторінки роботи з сесіями.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            request.session['value'] = value
    else:
        form = SessionForm()
    return render(request, 'members_app/session_page.html', {'form': form})
