# Generated by Django 4.2.2 on 2024-01-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobtracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="indicitive_services",
            field=models.ManyToManyField(blank=True, to="jobtracker.service"),
        ),
    ]
