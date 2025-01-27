from django.db import models
from .system_user import SystemUser
from .exercise import Exercise

class BrowsingHistory(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)