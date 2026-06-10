from django.contrib import admin

from library.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'library',
    )

    search_fields = (
        'title',
        'library__name',
    )

    list_filter = (
        'date',
        'library__name',
    )
