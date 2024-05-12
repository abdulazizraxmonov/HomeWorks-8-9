from django.db import models

class DictionaryLanguages(models.Model):
    language_name = models.CharField(max_length=255)

    def __str__(self):
        return self.language_name

class Dictionary(models.Model):
    code = models.CharField(max_length=255)
    language = models.ForeignKey(DictionaryLanguages, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word
