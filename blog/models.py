from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Snippet(models.Model):
    topic = models.CharField(max_length=100)
    branding_content = models.TextField()
    keywords = models.TextField()
    date_generated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted => their post also deleted as well 

    def __str__(self):
        return self.topic