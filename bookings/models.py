from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    canceled = models.BooleanField(default=False)
    cancel_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Canceled" if self.canceled else "Active"
        return f"{self.name} - {self.date} at {self.time} ({status})"