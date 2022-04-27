# Generated by Django 3.2.13 on 2022-04-27 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drscm', '0005_auto_20220427_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drscm.client')),
                ('fixed_travels', models.ManyToManyField(to='drscm.FixedTravel')),
                ('hourly_travels', models.ManyToManyField(to='drscm.HourlyTravel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drscm.project')),
                ('work_sessions', models.ManyToManyField(to='drscm.WorkSession')),
            ],
        ),
    ]
