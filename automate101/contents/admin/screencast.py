from django.contrib import admin

from contents.models import Screencast


@admin.register(Screencast)
class ScreencastModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'title',
        'description',
        'youtube_video_id',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    search_fields = (
        'title',
        'description',
        'youtube_video_id',
    )
