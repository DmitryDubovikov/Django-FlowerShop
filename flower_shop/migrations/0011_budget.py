# Generated by Django 4.2.4 on 2023-08-19 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0010_alter_occasion_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='минимальная цена')),
                ('max_price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='максимальная цена')),
            ],
            options={
                'verbose_name': 'бюджет',
                'verbose_name_plural': 'бюджеты',
            },
        ),
    ]
