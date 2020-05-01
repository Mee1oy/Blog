from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to='images/', null=True, blank=True)
    class Meta:
        ordering = ('-created_at',)
