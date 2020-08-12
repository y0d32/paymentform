# Generated by Django 3.1 on 2020-08-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditcard_number', models.CharField(max_length=16)),
                ('card_holder', models.CharField(max_length=30)),
                ('security_code', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]