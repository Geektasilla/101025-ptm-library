from django.contrib import admin

from library.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'country',
    )

    search_fields = (
        'name',
        'city',
        'country',
    )
