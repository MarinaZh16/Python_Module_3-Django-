# Generated by Django 3.0.6 on 2020-06-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_purchase_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='return',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'NEW'), (2, 'DECLINED'), (3, 'APPROVED')], default=1),
        ),
    ]
