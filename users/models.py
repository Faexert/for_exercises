from django.contrib.auth.models import AbstractUser # importing AbstractUser from Django's built-in authentication models

class User(AbstractUser): # its own user class inherited from AbstractUser
    pass
