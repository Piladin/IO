from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from api.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

SystemUser = get_user_model()
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
    
