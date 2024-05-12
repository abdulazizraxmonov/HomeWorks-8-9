from django.db import models

class AllAnnouncements(models.Model):
    data_published = models.DateTimeField()
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "All Announcements"