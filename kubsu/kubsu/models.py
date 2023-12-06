from django.db import models
from Account.models import *

#Here relations Faculties, Specials, Groups and relation many-to-many fac_teacher
class Faculties(models.Model):
    id_faculty = models.PositiveIntegerField(primary_key=True)
    name_faculty = models.TextField()

class Specials(models.Model):
    id_spec = models.PositiveIntegerField(primary_key=True)
    name_spec = models.TextField()
    id_faculty = models.ForeignKey(
        'kubsu.Faculties',
        on_delete=models.CASCADE
    )

class Groups(models.Model):
    num_group = models.TextField(primary_key=True)
    id_spec = models.ForeignKey(
        'kubsu.Specials',
        on_delete=models.CASCADE

    )

class Fac_teacher(models.Model):
    class Meta:
        unique_together = (('id_faculty', 'id_teacher'),)

    id_teacher = models.ForeignKey(
        'Account.Teachers',
        on_delete=models.CASCADE,
        default=0
    )
    id_faculty = models.ForeignKey(
        'kubsu.Faculties',
        on_delete=models.CASCADE
    )
    