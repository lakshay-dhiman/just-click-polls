# Generated by Django 3.1.2 on 2020-10-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_poll_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='options',
            field=models.JSONField(default=dict),
        ),
    ]
