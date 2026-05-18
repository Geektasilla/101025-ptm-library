from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )
    surname = models.CharField(
        max_length=100,
    )
    date_for_birth = models.DateTimeField(
        null=True,
        blank=True
    )

    profile = models.URLField(
        max_length=100,
        null=True,
        blank=True,
    )
    deleted = models.BooleanField(
        default=False,
    )
    rating = models.FloatField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
    )


    def __str__(self):
        return f'{self.name} {self.surname}'



