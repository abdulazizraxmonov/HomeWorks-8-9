from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    profile_img = models.ImageField(upload_to='department_profiles/', default='default_profile.jpg')

    def __str__(self):
        return self.name