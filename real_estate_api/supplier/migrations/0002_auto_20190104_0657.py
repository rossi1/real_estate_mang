# Generated by Django 2.0 on 2019-01-04 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierlisting',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='supplierlisting',
            name='longitude',
        ),
    ]
