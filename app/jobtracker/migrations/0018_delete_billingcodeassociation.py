# Generated by Django 5.0.3 on 2024-03-20 11:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("jobtracker", "0017_billingcode_client_billingcode_region_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BillingCodeAssociation",
        ),
    ]