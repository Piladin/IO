from rest_framework import viewsets, filters, status
from .models import Exercise, SystemUser
from .serializers import ExerciseSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer, SystemUserSerializer
from django.contrib.auth import get_user_model
from .recommendation_logic import recommend_exercises
from .permissions import IsAdminOrReadOnly


SystemUser = get_user_model()

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
    
class RecommendedExercisesView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return recommend_exercises(user)

    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        print("Request data:", request.data)  # Debug print
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("Error saving user:", str(e))  # Debug print
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print("Serializer errors:", serializer.errors)  # Debug print
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
