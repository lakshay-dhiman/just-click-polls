from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    poll_title = models.TextField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    options = models.JSONField(default=dict)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    votes = models.JSONField(default=dict)


class Uservoted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    option_chosen = models.IntegerField(null=True)
