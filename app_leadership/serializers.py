from rest_framework import serializers
from .models import Rahbariyat

class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = '__all__'