# Generated by Django 3.1 on 2020-08-11 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0005_auto_20200811_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='card',
            name='updated_at',
        ),
    ]
