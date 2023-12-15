# Generated by Django 4.2.5 on 2023-12-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_elevatorsystem_max_floor_cannot_be_zero"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="elevatorrequest",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("requested_floor__lt", models.F("destination_floor")),
                    ("requested_floor__gt", models.F("destination_floor")),
                    _connector="OR",
                ),
                name="requested_floor_and_destination_floor_cannot_be_same",
            ),
        ),
    ]
