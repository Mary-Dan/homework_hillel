from django.urls import path
from . import views
from .views import CourseCreateView
# визначаємо шляхи URL для нашого додатку
urlpatterns = [
    path('', views.courses_page, name='courses_page'),
]
# визначаємо шляхи URL до CourseCreateView
urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course_create'),
]