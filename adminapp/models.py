from django.db import models

# Create your models here.

class PlayTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time)
