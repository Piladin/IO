from rest_framework import generics
from api.serializers import ExerciseSerializer
from api.recommendation_logic import recommend_exercises
from rest_framework.permissions import IsAuthenticated

class RecommendedExercisesView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return recommend_exercises(user)