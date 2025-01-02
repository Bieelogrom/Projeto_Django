from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid



class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
        
    
