# Generated by Django 3.0.6 on 2020-06-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_purchase_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.FloatField(default=0, verbose_name='Cost'),
        ),
    ]