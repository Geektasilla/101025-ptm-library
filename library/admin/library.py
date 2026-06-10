from django.contrib import admin

from library.models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
    )

    search_fields = (
        'name',
        'location',
    )

