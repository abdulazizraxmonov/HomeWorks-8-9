from rest_framework import serializers
from .models import Standard, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'
        

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        standard = Standard.objects.create(**validated_data)
        for photo_data in photos_data:
            image_url = photo_data.pop('image')  
            photo = Photo.objects.create(standard=standard, **photo_data)
            photo.image = image_url  
            photo.save()
        return standard