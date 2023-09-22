from django.db import models

# Create your models here.

class PlayTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)
