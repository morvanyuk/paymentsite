import datetime

from django.db import models

class Paidusers(models.Model):
    user = models.CharField(max_length=255, null=True, blank=True)
    total_sum = models.FloatField(null=True, blank=True)
    date = datetime.datetime.now()
    discord_name = models.CharField(max_length=255, null=True, blank=True)
    succesed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user
    
class ContactData(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    data = models.CharField(max_length=300, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name