from django.contrib.auth.models import User
from django.db import models
from project.members_app.models import UserEnrollment


class Course(models.Model):
    title = models.CharField(max_length=255)
    students = models.ManyToManyField('members_app.User', through=UserEnrollment)

    def __str__(self):
        return self.title



