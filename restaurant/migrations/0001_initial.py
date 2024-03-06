# Generated by Django 5.0.2 on 2024-03-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField(default=6)),
                ('BookingDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField(default=5)),
            ],
        ),
    ]
