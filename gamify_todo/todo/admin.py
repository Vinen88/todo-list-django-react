from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created_date', 'due_date', 'points', 'completed')

# Register your models here.
  
admin.site.register(Todo, TodoAdmin)