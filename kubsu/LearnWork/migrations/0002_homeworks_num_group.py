# Generated by Django 4.2.6 on 2023-12-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kubsu', '0001_initial'),
        ('LearnWork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworks',
            name='num_group',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='kubsu.groups'),
        ),
    ]
