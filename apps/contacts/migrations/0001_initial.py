# Generated by Django 4.1.6 on 2023-02-07 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AddressBook",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("first_name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(blank=True, max_length=256, null=True)),
                ("birthday", models.DateField(blank=True, null=True)),
                (
                    "address_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacts.addressbook",
                    ),
                ),
            ],
        ),
    ]
