from django.urls import path
from . import views
# визначаємо шляхи URL для нашого додатку
urlpatterns = [
    path('', views.courses_page, name='courses_page'),
]