from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'
