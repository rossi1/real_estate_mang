# Generated by Django 2.0.6 on 2019-01-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20181230_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelinfo',
            name='hotel_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
