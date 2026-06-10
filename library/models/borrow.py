from datetime import datetime

from django.db import models
from django.utils import timezone


class Borrow(models.Model):
    member = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    book = models.ForeignKey(
        "Book",
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    library = models.ForeignKey(
        "Library",
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    issue_date = models.DateField(
        default=timezone.now,
    )
    return_plane_date = models.DateField(
        verbose_name='Планируемая дата возврата',
    )
    return_actual_date = models.DateField(
        verbose_name='Фактическая дата возврата',
        null=True,
        blank=True,
    )

    is_returned = models.BooleanField(
        verbose_name='Книгу вернули',
        default=False
    )

    def check_date_is_returned(self):
        if self.is_returned and self.return_actual_date < datetime.now():
            return False
        return True

    def __str__(self):
        return f"{self.member.username}. {self.book.name} ({self.library.name})"

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'
