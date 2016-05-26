from django.contrib import admin

from contents.models import Tag


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    search_fields = (
        'name',
    )
