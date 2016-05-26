from django.db import models


class Screencast(models.Model):

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    youtube_video_id = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
