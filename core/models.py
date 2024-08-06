from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Wine(models.Model):
    producer = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    year = models.IntegerField()
    style = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    months = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producer} {self.variety} {self.year}"

    def get_absolute_url(self):
        return reverse('wine-index') # todo: change to wine-detail (add kwargs)