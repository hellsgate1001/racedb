from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=255)
    download = models.URLField(max_length=255)

    def __str__(self):
        return self.name
