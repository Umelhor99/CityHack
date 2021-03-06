# Generated by Django 2.1.2 on 2019-05-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0010_auto_20190511_2238'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('monthly_waste', models.FloatField(default=-1.0)),
                ('divisions', models.ManyToManyField(blank=True, to='nodes.Division')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='members',
            field=models.ManyToManyField(blank=True, to='users.Member'),
        ),
    ]
