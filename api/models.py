from django.db import models

class UploadHistory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255)
    total_count = models.IntegerField()
    avg_temp = models.FloatField()
    
    class Meta:
        ordering = ['-timestamp'] # Keeps newest first
