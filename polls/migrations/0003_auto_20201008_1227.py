# Generated by Django 3.1.2 on 2020-10-08 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_poll_poll_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='options',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='time_created',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='votes',
        ),
    ]