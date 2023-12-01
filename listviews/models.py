from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  #สามารถใช้ Django's built-in User model ได้
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

