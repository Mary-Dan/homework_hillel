from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class YourModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MedicalInstitution(YourModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Patient(YourModel):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)  # Явное указание типа User
    medical_institution = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.user.username


class Doctor(YourModel):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_institution = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Consultation(YourModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medical_institution = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(help_text="Duration in minutes")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Consultation for {self.patient.user.username} with {self.doctor.user.username} at {self.date}"


class UserLoginLog(models.Model):
    """Модель для реєстрації входу користувачів у систему."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
