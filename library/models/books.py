from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    libraries = models.ManyToManyField(
        'Library',
        related_name='books'
    )
    description= models.TextField(
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    discounted_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    pages = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(1500)],
        null=True,
        blank=True
    )
    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    owner = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )
    published_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.name
