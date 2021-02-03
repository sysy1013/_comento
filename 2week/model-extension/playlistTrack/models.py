from django.db import models
from Invoicline import models

class Comment(modesl.Model):
    id = models.IntegerField(default = 0)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

