from django.db import models
from kubsu.models import *

class Students(models.Model):
    id_student = models.TextField(primary_key=True)
    last_name = models.TextField()
    name = models.TextField()
    patronym = models.TextField()

    num_group = models.ForeignKey(
        'kubsu.Groups',
        on_delete=models.CASCADE,
        default='0'
    )


class Teachers(models.Model):
    id_teacher = models.TextField(primary_key=True)
    last_name = models.TextField()
    name = models.TextField()
    patronym = models.TextField()

    email = models.TextField(null=False, unique=True)
    academic_title = models.TextField()
    department = models.TextField()

class Decan(models.Model):
    id_faculty = models.ForeignKey(
        'kubsu.Faculties',
        primary_key=True,
        on_delete=models.CASCADE,
        default=0
    )
    login = models.TextField()
    password = models.TextField()
    
