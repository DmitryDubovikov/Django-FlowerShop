# Generated by Django 4.2.4 on 2023-08-17 12:45

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0004_alter_flower_price_alter_flowerset_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='имя')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'консультация',
                'verbose_name_plural': 'консультации',
            },
        ),
    ]
