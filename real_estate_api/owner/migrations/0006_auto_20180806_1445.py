# Generated by Django 2.0 on 2018-08-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_auto_20180805_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlisting',
            name='contact_profile_photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertylisting',
            name='contact_name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertylisting',
            name='contact_profile_photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
