from django.db import models

class Reglament(models.Model):
    nomer = models.CharField(max_length=20)
    belgilanishi = models.CharField(max_length=20)
    nomi = models.CharField(max_length=200)
    hujjat = models.FileField(upload_to='reglament_files/') 

    def __str__(self):
        return f"{self.nomer} - {self.nomi}"