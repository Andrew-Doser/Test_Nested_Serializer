from django.db import models

# Create your models here.
class status(models.Model):
    name    = models.TextField(blank=False)
    