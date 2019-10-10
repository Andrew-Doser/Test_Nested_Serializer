from django.db import models
from statuses.models import status


# Create your models here.
class post(models.Model):
    title = models.TextField()
    description = models.TextField()
    status = models.ForeignKey(status, on_delete=models.CASCADE)
