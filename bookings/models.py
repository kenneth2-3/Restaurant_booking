from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    canceled = models.BooleanField(default=False)
    cancel_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Time periods variations
    TIME_PERIODS = (
        (0, '9:00-9:45'),
        (1, '10:00-10:45'),
        (2, '11:00-11:45'),
        (3, '14:00-14:45'),
        (4, '15:00-15:45'),
        (5, '16:00-16:45'),
        (6, '17:00-17:45'),
        (7, '18:00-18:45'),
    )

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("Booking date cannot be in the past")
        if self.date == datetime.date.today() and self.time < datetime.datetime.now().time():
            raise ValidationError("Booking time cannot be in the past")
        super().save(*args, **kwargs)

