from django.db import models


# Create your models here.
class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Nowe"
        IN_PROGRESS = "in_progress", "w trakcie"
        CLOSED = "closed", "Zamknięte"

    class Priority(models.TextChoices):
        LOW = "low", "Niski"
        MEDIUM = "medium", "Średni"
        HIGH = "high", "Wyskoki"

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.MEDIUM
    )

    created_at = models.DateTimeField(auto_now_add=True)
