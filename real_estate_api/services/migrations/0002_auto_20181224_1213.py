# Generated by Django 2.0 on 2018-12-24 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceslisting',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='serviceslisting',
            name='longitude',
        ),
    ]
