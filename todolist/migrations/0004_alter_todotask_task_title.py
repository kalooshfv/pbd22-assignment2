# Generated by Django 4.1 on 2022-09-29 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todotask_task_isfinished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='task_title',
            field=models.CharField(max_length=64),
        ),
    ]
