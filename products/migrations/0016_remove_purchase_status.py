# Generated by Django 3.0.6 on 2020-06-30 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_return_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='status',
        ),
    ]