from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description =  models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title