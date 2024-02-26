from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course
from django.urls import reverse_lazy
from django.views.generic import CreateView


@login_required
def courses_page(request):
    """
    Представлення для сторінки, доступне тільки користувачам.

    Parameters:
    request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

    """
    return render(request, 'courses_app/courses_page.html')


class CourseCreateView(CreateView):
    """
        Представлення для сторінки, доступне тільки користувачам.

        Parameters:
        request (HttpRequest): Об'єкт запиту, який містить дані від клієнта.

        """
    model = Course
    fields = ['title']
    success_url = reverse_lazy('course_create')
