from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=16,
        verbose_name="이름",
    )

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
