from django.urls import path
from messenger_js.messenger import views

urlpatterns = [
    path('', views.chats, name='chats'),
    path('chat/<int:chat_id>/', views.chat, name='chat'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('chat/<int:chat_id>/add_user/', views.add_user, name='add_user'),
    path('message/<int:message_id>/edit/', views.edit_message, name='edit_message'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('chat/<int:chat_id>/delete_user/<int:user_id>/', views.delete_user, name='delete_user')
]
