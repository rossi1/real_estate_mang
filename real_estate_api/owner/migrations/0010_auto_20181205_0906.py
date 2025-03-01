# Generated by Django 2.0 on 2018-12-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0009_auto_20181205_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlisting',
            name='contact_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='contact_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='contact_profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
