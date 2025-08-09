from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
