# Generated by Django 2.0.6 on 2018-12-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotellisting',
            name='state',
            field=models.CharField(max_length=250),
        ),
    ]
