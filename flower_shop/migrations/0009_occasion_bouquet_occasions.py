# Generated by Django 4.2.4 on 2023-08-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0008_order_total_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='bouquet',
            name='occasions',
            field=models.ManyToManyField(related_name='bouquets', to='flower_shop.occasion', verbose_name='события'),
        ),
    ]
