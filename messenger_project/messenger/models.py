from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def get_chats(self):
        chats = Chat.objects.filter(users=self)
        return chats

    def add_to_chat(self, chat):
        chat.add_user(self)

    def remove_from_chat(self, chat):
        chat.remove_user(self)

    def get_messages(self):
        messages = Message.objects.filter(author=self)
        return messages


class Chat(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(CustomUser, related_name='chats')

    def __str__(self):
        return self.name

    def add_user(self, user):
        self.users.add(user)

    def remove_user(self, user):
        self.users.remove(user)


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def can_edit_or_delete(self, user):
        if user.is_superuser:
            return True
        if user == self.author:
            if self.created_at.date() == timezone.now().date():
                return True
        return False


class User:
    pass