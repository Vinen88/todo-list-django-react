from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title