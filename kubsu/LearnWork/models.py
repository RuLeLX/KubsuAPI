from django.db import models
from kubsu.models import *
from Account.models import *
from LearnData.models import *

class HomeWorks(models.Model):
    class Meta:
        unique_together = (('id_teacher', 'id_discip'),)

    id_teacher = models.ForeignKey(
        'Account.Teachers',
        on_delete=models.CASCADE

    )
    id_discip = models.ForeignKey(
        'LearnData.Desciplines',
        on_delete=models.CASCADE
    )

    num_group = models.ForeignKey(
        'kubsu.Groups',
        on_delete = models.CASCADE,
        default='0'
    )

    work = models.TextField()

class Progress(models.Model):
    class Meta:
        unique_together = (('id_student', 'id_discip'),)
    
    id_student = models.ForeignKey(
        'Account.Students',
        on_delete=models.CASCADE
    )
    id_discip = models.ForeignKey(
        'LearnData.Desciplines',
        on_delete=models.CASCADE
    )

    score_and_traffic = models.TextField() #this is encrypted json with score and traffic students