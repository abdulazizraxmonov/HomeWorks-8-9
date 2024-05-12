from django.db import models

class Standard(models.Model):
    code = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.code}: {self.year}"

class Photo(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='standards_photos')

    def __str__(self):
        return f"Photo for {self.standard}"