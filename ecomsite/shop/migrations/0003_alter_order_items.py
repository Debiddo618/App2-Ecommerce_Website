# Generated by Django 4.2.6 on 2023-10-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="items",
            field=models.CharField(max_length=1000),
        ),
    ]
