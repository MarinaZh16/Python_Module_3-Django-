# Generated by Django 3.0.6 on 2020-06-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200628_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='return',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
