from django.db import models


class Screencast(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="제목",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="설명",
    )

    youtube_video_id = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        verbose_name="유튜브 VIDEO ID",
    )

    class Meta:
        verbose_name = "영상"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
