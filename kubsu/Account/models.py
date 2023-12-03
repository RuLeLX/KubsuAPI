from django.db import models
from kubsu.models import *

class Students(models.Model):
    id_student = models.TextField(primary_key=True)
    last_name = models.TextField()
    name = models.TextField()
    patronym = models.TextField()

    # series_password = models.PositiveIntegerField(unique=True)
    # num_password = models.PositiveIntegerField(unique=True)
    # SNILS = models.TextField(unique=True)

    num_group = models.ForeignKey(
        'kubsu.Groups',
        on_delete=models.CASCADE
    )


class Teachers(models.Model):
    id_teacher = models.TextField(primary_key=True)
    last_name = models.TextField()
    name = models.TextField()
    patronym = models.TextField()

    academic_title = models.TextField()
    department = models.TextField()

    
