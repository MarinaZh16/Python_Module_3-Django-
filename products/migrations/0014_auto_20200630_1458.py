# Generated by Django 3.0.6 on 2020-06-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_purchase_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='buyer',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='is_cancelled',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product_images/'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'NEW'), (2, 'CANCELLED'), (3, 'DECLINED'), (4, 'APPROVED'), (5, 'SUCCESS')], default=1),
        ),
        migrations.AddField(
            model_name='return',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'NEW'), (2, 'DECLINED'), (3, 'APPROVED')], default=1),
        ),
    ]
