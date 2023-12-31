# Generated by Django 3.2.19 on 2023-10-30 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('digitapp', '0009_alter_project_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='lab',
            name='fields',
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 30, 5, 57, 40, 23561, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='lab',
            name='fields',
            field=models.ManyToManyField(related_name='lab', to='digitapp.Field'),
        ),
    ]
