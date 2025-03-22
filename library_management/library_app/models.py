from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Avoid conflicts with Django's default User model
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="admin_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="admin_users",
        blank=True
    )

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
