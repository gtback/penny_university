from django.db import models
from django.utils import timezone


class PennyChat(models.Model):
    DRAFT_STATUS = 1
    SHARED_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (SHARED_STATUS, 'Shared')
    )

    title = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(null=True)
    invitees = models.TextField()
    channels = models.TextField()
    view = models.TextField()
    user = models.TextField()
    user_tz = models.TextField()
    template_channel = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT_STATUS)


class FollowUp(models.Model):
    penny_chat = models.ForeignKey('PennyChat', related_name='follow_ups', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.TextField()

