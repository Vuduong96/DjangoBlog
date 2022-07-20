from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Branding(models.Model):
    topic = models.CharField(max_length=100)
    branding_content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted => their post also deleted as well 

    def __str__(self):
        return self.topic

class Keyword(models.Model):
    branding = models.ForeignKey(Branding, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=255, null=False, 
                            blank=False, default=['coffee','latte'])