from rest_framework import serializers
from api.models import BrowsingHistory

class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrowsingHistory
        fields = ['user', 'exercise', 'timestamp']