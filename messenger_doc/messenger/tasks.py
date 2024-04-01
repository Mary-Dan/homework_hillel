from celery import shared_task
from django.core.mail import send_mail
import time
from datetime import datetime

# Визначаємо функцію-задачу для відправки електронного листа з привітанням користувачеві
@shared_task
def send_registration_email(user_email):
    send_mail(
        'Welcome to our website!',
        'Thank you for registering on our website.',
        'noreply@example.com',
        [user_email],
        fail_silently=False,
    )

# Визначаємо функцію-задачу, яка симулює довгий процес обробки даних
@shared_task
def long_running_task():
    time.sleep(10)
    print("Довга обробка даних завершена!")

# Визначаємо функцію-задачу для виведення поточного часу у консоль
@shared_task
def print_time():
    print(datetime.now())
