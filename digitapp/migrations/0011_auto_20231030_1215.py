# Generated by Django 3.2.19 on 2023-10-30 06:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('digitapp', '0010_auto_20231030_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='digitapp.field'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 30, 6, 15, 4, 838649, tzinfo=utc)),
        ),
    ]
