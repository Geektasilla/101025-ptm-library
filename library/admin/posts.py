from django.contrib import admin

from library.models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'moderated',
        'library',
        'published_date',
    )

    search_fields = (
        'title',
        'author__last_name',
    )

    list_filter = (
        'moderated',
        'published_date',
    )
