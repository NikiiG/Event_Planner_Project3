# Generated by Django 4.2.3 on 2023-08-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0004_alter_vendor_pricing"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="category",
        ),
        migrations.RemoveField(
            model_name="event",
            name="vendors",
        ),
        migrations.AddField(
            model_name="event",
            name="Category",
            field=models.CharField(
                choices=[("B", "Bootcamp"), ("S", "Social Event")],
                default="B",
                max_length=1,
            ),
        ),
    ]
