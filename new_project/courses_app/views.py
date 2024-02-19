from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def courses_page(request):
    """
    Представлення для сторінки, доступне тільки користувачам.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    return render(request, 'courses_app/courses_page.html')

