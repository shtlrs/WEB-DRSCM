# Generated by Django 3.2.13 on 2022-04-28 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drscm", "0008_worksessionproxy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="hourly_rate",
        ),
    ]
