from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Detail', kwargs={'pk':self.pk})



