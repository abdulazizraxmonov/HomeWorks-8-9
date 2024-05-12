from django.db import models

class elstandardsFound(models.Model):
    name = models.CharField(max_length=200)
    document_number = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    approved_year = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} (Document Number: {self.document_number})"

class elstandardsFoundPhoto(models.Model):
    standard = models.ForeignKey(elstandardsFound, on_delete=models.CASCADE)
    file = models.FileField(upload_to='elstandardsfound_files')

    def __str__(self):
        return f"File for {self.standard}"
