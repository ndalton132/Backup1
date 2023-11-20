# Generated by Django 3.2.13 on 2023-11-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('comments', models.TextField()),
                ('gasStationAddr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gas_Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('regular_gas_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('premium_gas_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diesel_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
