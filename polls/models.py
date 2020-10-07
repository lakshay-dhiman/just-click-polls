from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    poll_title = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    options = ArrayField(models.CharField(max_length=50), size=8, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    votes = ArrayField(models.CharField(max_length=20), size=8, null=True)


class Uservoted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    option_chosen = models.IntegerField()
