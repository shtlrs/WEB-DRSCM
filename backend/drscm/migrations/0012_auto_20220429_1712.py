# Generated by Django 3.2.13 on 2022-04-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drscm", "0011_auto_20220428_0140"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="fixed_travels",
            field=models.ManyToManyField(blank=True, to="drscm.FixedTravel"),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="hourly_travels",
            field=models.ManyToManyField(blank=True, to="drscm.HourlyTravel"),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="work_sessions",
            field=models.ManyToManyField(blank=True, to="drscm.WorkSession"),
        ),
    ]
