# Generated by Django 3.0.6 on 2020-06-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_return_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.FloatField(default=1, max_length=7, verbose_name='Cost'),
        ),
    ]
