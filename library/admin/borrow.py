from django.contrib import admin

from library.models import Borrow


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = (
        'member',
        'book',
        'issue_date',
        'return_plane_date',
        'return_actual_date',
        'is_returned',
    )

    search_fields = (
        'member__last_name',
        'book__name',
    )

    list_filter = (
        'is_returned',
        'issue_date',
    )
