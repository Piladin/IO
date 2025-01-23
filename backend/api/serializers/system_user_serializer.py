from rest_framework import serializers
from api.models import SystemUser

class SystemUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']