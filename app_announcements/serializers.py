from rest_framework import serializers
from .models import AllAnnouncements

class AllAnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllAnnouncements
        fields = '__all__'