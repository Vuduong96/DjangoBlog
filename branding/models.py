from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import F, Max

class Branding(models.Model):
    topic = models.CharField(max_length=100)
    branding_content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted => their post also deleted as well 

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('branding-detail', kwargs={'pk':self.pk})

    

