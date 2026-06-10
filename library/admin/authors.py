from django.contrib import admin

from library.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'surname',
        'date_for_birth',
        'rating',
    )

    search_fields = (
        'name',
        'surname'
    )

    list_filter = (
        'deleted',
    )
