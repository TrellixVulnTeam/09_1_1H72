# Generated by Django 2.1.1 on 2018-09-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroNine', '0002_auto_20180914_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='direct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='notice',
        ),
        migrations.RemoveField(
            model_name='product',
            name='start_time',
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.BooleanField(default=False),
        ),
    ]
