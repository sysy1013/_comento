from django.db import models
from playlistTrack import models

class Todo(modesl.Model):
    id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)