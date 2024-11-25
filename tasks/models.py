from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OAuthSettings(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    redirect_uri = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OAuth Settings (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"

class Invitation(models.Model):
    email = models.EmailField(unique=True)  # Email of the invited user
    invited_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the invitation was created
    is_used = models.BooleanField(default=False)  # Track if the invitation has been used

    def __str__(self):
        return f"Invitation for {self.email}"

