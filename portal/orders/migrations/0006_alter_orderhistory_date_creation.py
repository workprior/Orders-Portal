# Generated by Django 4.2.11 on 2024-05-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_orderhistory_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderhistory",
            name="date_creation",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
