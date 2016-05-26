from django.db import models


class Chapter(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="제목",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="설명",
    )

    class Meta:
        verbose_name = "챕터"
        verbose_name_plural = verbose_name
