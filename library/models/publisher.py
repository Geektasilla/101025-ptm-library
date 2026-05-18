from django.db import models


class Publisher(models.Model):
    name = models.CharField(
        max_length=100
    )
    about = models.TextField(
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=100,
    )


    def __str__(self):
        return self.name



