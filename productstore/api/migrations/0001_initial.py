# Generated by Django 5.1 on 2024-08-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("category", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("price", models.CharField(max_length=255)),
                ("mrp", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("Fit", models.CharField(max_length=255)),
                ("Fabric", models.CharField(max_length=255)),
                ("Neck", models.CharField(max_length=255)),
                ("Sleeve", models.CharField(max_length=255)),
                ("Pattern", models.CharField(max_length=255)),
                ("Length", models.CharField(max_length=255)),
            ],
        ),
    ]
