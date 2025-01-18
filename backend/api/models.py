from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    description = models.TextField()
    tutorial = models.TextField()

    def __str__(self):
        return self.name
    
class SystemUser(AbstractUser):

    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set", 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  
        blank=True,
    )
    
class BrowsingHistory(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)