# Generated by Django 3.2.2 on 2021-05-12 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
