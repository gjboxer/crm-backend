# Generated by Django 4.2.3 on 2024-01-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0002_lead_description_lead_hotel_address_lead_hotel_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="country",
            field=models.CharField(default="", max_length=30),
        ),
    ]