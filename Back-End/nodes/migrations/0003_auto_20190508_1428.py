# Generated by Django 2.1.2 on 2019-05-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_nodemcu_current_waste'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodemcu',
            name='power',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='nodemcu',
            name='current_waste',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='nodemcu',
            name='monthly_budget',
            field=models.FloatField(default=-1.0),
        ),
    ]
