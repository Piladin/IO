from rest_framework import serializers
from api.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'muscle_group', 'difficulty', 'exercise_type', 'description', 'tutorial']