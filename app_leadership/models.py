from django.db import models

class Rahbariyat(models.Model):
    ism = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    qabul_kunlari = models.CharField(max_length=50)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    bakalavr_mutaxassisligi = models.TextField(blank=True, null=True)
    magistratura_mutaxassisligi = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='rahbariyat_profile_images/', blank=True, null=True)

    def __str__(self):
        return self.ism