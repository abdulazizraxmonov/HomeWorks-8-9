from django.db import models

class News(models.Model):
    news_datetime = models.DateTimeField()
    news_name = models.CharField(max_length=255)
    news_description = models.TextField()
    news_text = models.TextField()
    news_photo = models.ImageField(upload_to='news_photos/')
    
    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name_plural = "News" 