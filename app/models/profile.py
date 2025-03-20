from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = {"m": "Male", "v": "Female", "u": "Undefined"}

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default="u", max_length=10)
    github_username = models.CharField(null=True, blank=True, max_length=255)
    picture = models.TextField(null=True, blank=True)
