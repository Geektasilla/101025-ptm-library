from django.contrib import admin

from library.models import Author


# Register your models here.
@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
        'date_for_birth',
        'deleted',
        'rating'
    ]

    list_filter = [
        'deleted',
        'rating'
    ]

    search_fields = [
        'name',
        'surname',
        'profile'
    ]

    list_editable = [
        'deleted',
        'rating'
    ]

    list_per_page = 50




