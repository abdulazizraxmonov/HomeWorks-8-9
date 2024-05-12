from rest_framework import serializers
from .models import DictionaryLanguages, Dictionary

class DictionaryLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictionaryLanguages
        fields = '__all__'

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
