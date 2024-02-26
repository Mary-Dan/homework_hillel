from django.urls import path
from . import views
from .views import UserEnrollmentCreateView

# визначаємо шляхи URL для нашого додатку
urlpatterns = [
    path('input/', views.input_page, name='input_page'),
    path('display/', views.display_input, name='display_input'),
    path('session/', views.session_page, name='session_page'),
]
# визначаємо шляхи URL до UserEnrollmentCreateView
urlpatterns = [
    path('enroll/', UserEnrollmentCreateView.as_view(), name='enroll_student'),
]
