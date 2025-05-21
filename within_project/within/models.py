from django.db import models
from django.utils import timezone

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        ('angry', 'Angry'),
        ('anxious', 'Anxious'),
    ]
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.mood} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
