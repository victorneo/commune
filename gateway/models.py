from django.db import models


class Event(models.Model):
    op = models.IntegerField(null=False)
    d = models.TextField(null=True)
    s = models.IntegerField(null=True)
    t = models.TextField(null=True)
