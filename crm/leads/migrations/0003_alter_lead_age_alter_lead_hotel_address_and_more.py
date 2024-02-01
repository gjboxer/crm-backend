# Generated by Django 4.2.3 on 2024-02-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="age",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="lead",
            name="hotel_address",
            field=models.CharField(blank=True, default="", max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="lead",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="lead",
            name="url",
            field=models.CharField(blank=True, default="", max_length=30, null=True),
        ),
    ]
