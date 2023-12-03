from django.db import models
from kubsu.models import *
from Account.models import *

class Desciplines(models.Model):
    id_discip = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()

    id_spec = models.ForeignKey(
        'kubsu.Specials',
        on_delete=models.CASCADE
    )

class Lessons(models.Model):
    class Meta:
        unique_together = (('time_interval', 'id_teacher', 'weekday'),)

    id_teacher = models.ForeignKey(
        'Account.Teachers',
        on_delete=models.CASCADE
    )
    time_interval = models.TextField()
    weekday = models.TextField()

    id_discip = models.ForeignKey(
        'LearnData.Desciplines',
        on_delete=models.CASCADE
    )
    num_group = models.ForeignKey(
        'kubsu.Groups',
        on_delete=models.CASCADE
    )
