# Generated by Django 4.2.5 on 2023-11-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "store_app",
            "0004_alter_product_description_alter_product_information_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact_us",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("subject", models.CharField(max_length=300)),
                ("message", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]