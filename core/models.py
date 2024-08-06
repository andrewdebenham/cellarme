from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Wine(models.Model):
    producer = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    year = models.IntegerField()
    style = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    storage_date = models.DateField()
    months_for_storage = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producer} {self.variety} {self.year}"

    def get_absolute_url(self):
        return reverse('wine-index') # todo: change to wine-detail (add kwargs)

    @property
    def ageing_progress(self):
        if self.storage_date:
            today = timezone.now().date()
            time_stored = today - self.storage_date
            total_days = self.months_for_storage * 30
            progress = (time_stored.days / total_days) * 100
            return min(progress, 100)
        return 0