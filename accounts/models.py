from django.db import models

# Create your models here.
class User(models.Model):
    user_email = models.EmailField()
