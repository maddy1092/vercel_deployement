from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)