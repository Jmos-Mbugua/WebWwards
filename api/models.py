from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class ApiPost(models.Model):
    title = models.CharField(max_length=255)
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class ApiProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

