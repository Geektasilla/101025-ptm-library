from django.db import models
from django.utils import timezone



class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        related_name='events'
    )
    books = models.ManyToManyField(
        'Book',
        related_name='events'
    )

    def __str__(self):
        return f'{self.title} - {self.date}'


class EventParticipant(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    member = models.ManyToManyField(
        'User',
        related_name='events'
    )
    registration_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        users = [user.username for user in self.member.all()]
        return f' EventParticipants: {users} {self.registration_date}'
