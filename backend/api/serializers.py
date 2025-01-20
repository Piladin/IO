from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, SystemUser, BrowsingHistory


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'muscle_group', 'difficulty', 'exercise_type', 'description', 'tutorial']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = SystemUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = SystemUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class SystemUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        
class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrowsingHistory
        fields = ['user', 'exercise', 'timestamp']