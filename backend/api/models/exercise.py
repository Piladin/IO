from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    description = models.TextField()
    tutorial = models.TextField()

    def __str__(self):
        return self.name
    