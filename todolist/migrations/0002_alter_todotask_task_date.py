# Generated by Django 4.1 on 2022-09-28 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='task_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]