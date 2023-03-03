from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    #profile_pic = models.ImageField(upload_to='profile_pics', blank=True) #maybe later
    points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username #maybe change this later