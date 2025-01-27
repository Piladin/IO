from rest_framework import viewsets, filters
from api.models import Exercise
from api.serializers import ExerciseSerializer
from rest_framework.permissions import IsAdminUser
from api.misc.custom_permissions import IsAdminOrReadOnly

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'muscle_group', 'exercise_type']
    ordering_fields = ['difficulty']
    permission_classes = [IsAdminOrReadOnly]

class ExerciseAdminViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAdminUser]