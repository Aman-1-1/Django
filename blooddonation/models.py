
from django.db import models

class logindoner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)  # store hashed password
    blood_type = models.CharField(max_length=10)
    is_donor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
