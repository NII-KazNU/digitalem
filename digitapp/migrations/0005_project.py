# Generated by Django 3.2.19 on 2023-06-08 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digitapp', '0004_alter_lab_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='digitapp.lab')),
            ],
        ),
    ]