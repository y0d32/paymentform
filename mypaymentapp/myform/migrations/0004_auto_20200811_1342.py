# Generated by Django 3.1 on 2020-08-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0003_auto_20200811_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
