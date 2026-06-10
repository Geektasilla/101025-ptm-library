from django.contrib import admin

from library.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'get_short_review',
        'book',
        'reviewer',
        'rating',
    )

    search_fields = (
        'content',
    )

    list_filter = (
        'rating',
    )

    @admin.display(description='review')
    def get_short_review(self, obj: Review):
        return obj if len(obj.content) <= 25 else f"{obj.content[:25]}..."
