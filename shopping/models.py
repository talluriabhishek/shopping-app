from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.FloatField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name