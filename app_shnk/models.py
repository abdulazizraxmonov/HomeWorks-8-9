from django.db import models

class Subsystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Document(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.code + " - " + self.title
