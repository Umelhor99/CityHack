# Generated by Django 2.2.1 on 2019-05-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_auto_20190508_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodemcu',
            old_name='current_waste',
            new_name='current_daily_waste',
        ),
        migrations.AddField(
            model_name='nodemcu',
            name='current_monthly_waste',
            field=models.FloatField(default=-1.0),
        ),
    ]
