# Generated by Django 3.0.6 on 2020-06-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200629_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
