from django.contrib import admin

from library.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'price',
        'publisher',
        'category',
    )

    search_fields = (
        'name',
        'description',
        'author__name',
    )

    list_filter = (
        'published_date',
        'category',
    )
