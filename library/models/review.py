from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.reviewer.username}. {self.rating}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
