# Generated by Django 3.1.2 on 2020-10-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_uservoted_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservoted',
            name='option_chosen',
            field=models.IntegerField(null=True),
        ),
    ]
