# Generated by Django 4.2.4 on 2023-08-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
    ]
