# Generated by Django 3.0.6 on 2020-06-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.FloatField(default=10000),
        ),
    ]
