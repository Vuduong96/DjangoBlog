from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Max

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user deleted => profile deleted (only 1 way)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'


