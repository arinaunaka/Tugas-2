# Generated by Django 4.1 on 2022-09-27 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
