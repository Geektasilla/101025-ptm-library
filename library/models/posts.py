from django.db import models
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=255, unique_for_date="published_date")
    post_text = models.TextField()
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    moderated = models.BooleanField(default=False)
    library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    published_date = models.DateField(default=timezone.now)
    updated_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
