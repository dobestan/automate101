from django.contrib import admin

from contents.models import Chapter


@admin.register(Chapter)
class ChapterModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'title',
        'description',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    search_fields = (
        'title',
        'description',
    )
