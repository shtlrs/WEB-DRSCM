# Generated by Django 3.2.13 on 2022-04-26 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drscm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourlyTravel',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.IntegerField(unique=True)),
                ('hours', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hourly_travels', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hourly_travels', to='drscm.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FixedTravel',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.IntegerField(unique=True)),
                ('occurrences', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_travels', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_travels', to='drscm.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
