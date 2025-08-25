from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField()
    time = models.IntegerField(choices=TIME_PERIODS, default=0)
    guests = models.PositiveIntegerField()
    canceled = models.BooleanField(default=False)
    cancel_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time')

    def clean(self):
        today = datetime.date.today()
        now = datetime.datetime.now().time()

        if self.date < today:
            raise ValidationError("Booking date cannot be in the past")

        if self.date == today:
            slot_label = dict(self.TIME_PERIODS).get(self.time)
            slot_start = datetime.datetime.strptime(slot_label.split("-")[0], "%H:%M").time()

            if slot_start < now:
                raise ValidationError("Booking time cannot be in the past")

        # Checks if another booking exists for same date + time
        if not self.canceled:
            conflict = Booking.objects.filter(
                date=self.date, time=self.time, canceled=False
            ).exclude(pk=self.pk).exists()
            if conflict:
                raise ValidationError("This time slot is already booked. Please select another one.")

    def __str__(self):
        return f"{self.name} - {self.date} {dict(self.TIME_PERIODS)[self.time]}"


