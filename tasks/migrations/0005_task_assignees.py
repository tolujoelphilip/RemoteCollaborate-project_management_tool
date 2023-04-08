# Generated by Django 4.1 on 2023-04-08 10:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_task_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
