# Generated by Django 2.0.6 on 2018-12-28 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181227_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelinfo',
            name='location',
        ),
    ]
