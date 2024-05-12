from rest_framework import serializers
from .models import Reglament

class ReglamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglament
        fields = '__all__'