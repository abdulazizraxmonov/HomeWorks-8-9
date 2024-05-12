from rest_framework import serializers
from .models import elstandardsFound, elstandardsFoundPhoto

class ElStandardFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = elstandardsFound
        fields = '__all__'


class elstandartsFoundPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = elstandardsFoundPhoto
        fields = '__all__'
