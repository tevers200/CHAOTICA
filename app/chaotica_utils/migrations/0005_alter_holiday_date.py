# Generated by Django 4.2.2 on 2023-09-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chaotica_utils", "0004_holiday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="holiday",
            name="date",
            field=models.DateField(db_index=True),
        ),
    ]
