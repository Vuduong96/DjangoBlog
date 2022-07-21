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

    def save(self):
        with User.atomic():
            count = Branding.objects.count()

            objects = User.objects.all()
            if count > 100:
                objects[0].delete()
                if count > 1:
                    objects.update(id=F('id') - 1)

            if not self.id and count > 0:
                objects = objects.refresh_from_db()  # Update QuerySet
                self.id = objects.annotate(max_count=Max('id')).max_count + 1
            elif not self.id and count == 0:
                self.id = 1

            self.save()

