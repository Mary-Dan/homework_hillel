from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.ChatList.as_view(), name='chat-list'),
    path('chats/<int:chat_id>/', views.ChatDetail.as_view(), name='chat-detail'),
    path('messages/', views.MessageList.as_view(), name='message-list'),
    path('messages/<int:message_id>/', views.MessageDetail.as_view(), name='message-detail'),
    path('messages/<int:message_id>/edit/', views.EditMessage.as_view(), name='edit-message'),
    path('messages/<int:message_id>/delete/', views.DeleteMessage.as_view(), name='delete-message'),
]
