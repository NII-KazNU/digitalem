# Generated by Django 3.2.19 on 2023-06-08 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='slug',
        ),
    ]
