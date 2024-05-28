from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('profile/', views.user_profile, name='user_profile'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('consultations/<int:consultation_id>/', views.consultation_detail, name='consultation_detail'),
    path('consultations/create/', views.create_consultation, name='create_consultation'),
    path('consultations/<int:consultation_id>/edit/', views.edit_consultation, name='edit_consultation'),
    path('consultations/<int:consultation_id>/delete/', views.delete_consultation, name='delete_consultation'),
    path('api/consultations/', views.ConsultationListAPIView.as_view(), name='api_consultation_list'),
]
