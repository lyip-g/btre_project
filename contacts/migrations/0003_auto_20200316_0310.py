# Generated by Django 3.0.4 on 2020-03-16 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200316_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing_is',
            new_name='listing_id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 16, 3, 9, 19, 349932)),
        ),
    ]
