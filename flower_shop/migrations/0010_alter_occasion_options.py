# Generated by Django 4.2.4 on 2023-08-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0009_occasion_bouquet_occasions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occasion',
            options={'verbose_name': 'повод', 'verbose_name_plural': 'поводы'},
        ),
    ]