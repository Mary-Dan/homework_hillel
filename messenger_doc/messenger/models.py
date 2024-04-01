from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.messages import success
import logging

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

logger = logging.getLogger(__name__)

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
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')

    def __str__(self):
        return self.content

    def can_edit_or_delete(self, user):
        if user.is_superuser:
            return True
        if user == self.author:
            if self.created_at.date() == timezone.now().date():
                return True
        return False

@receiver(post_save, sender=Message)
def log_message(sender, instance, **kwargs):
    if instance.recipient.is_superuser:
        success(request, "Ви успішно надіслали повідомлення суперюзеру")
        logger.info(f"User {instance.author.username} sent a message to superuser {instance.recipient.username}")
