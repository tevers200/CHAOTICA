# Generated by Django 4.2.2 on 2023-09-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chaotica_utils", "0003_alter_user_options_leaverecord"),
    ]

    operations = [
        migrations.CreateModel(
            name="Holiday",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(db_index=True)),
                ("country", models.CharField(max_length=10)),
                ("subdiv", models.CharField(max_length=10)),
                ("reason", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["-date"],
                "unique_together": {("date", "country", "subdiv")},
            },
        ),
    ]
