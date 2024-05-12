from django.db import models
from app_leadership.models import Rahbariyat

class Inquiry(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='FIO')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    rahbariyat = models.ForeignKey(Rahbariyat, on_delete=models.SET_NULL, related_name='inquiries', verbose_name='Rahbariyat', null=True)
    message = models.TextField(verbose_name='Murojaat matni')
    file = models.FileField(upload_to='inquiry_files/', verbose_name='Fayl biriktirish', blank=True, null=True)

    def __str__(self):
        return self.fullname
