from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500, blank=True) #blank=True for optional description
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    points = models.IntegerField(default=10)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['due_date']