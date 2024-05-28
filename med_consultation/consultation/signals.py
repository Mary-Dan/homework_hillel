
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserLoginLog


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Записує в базу даних час входу користувача."""
    UserLoginLog.objects.create(user=user)
