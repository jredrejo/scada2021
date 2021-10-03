# Generated by Django 3.2.7 on 2021-10-02 18:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tags",
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
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("direccion", models.CharField(max_length=100)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("I", "Integer"),
                            ("F", "Float"),
                            ("b", "Bit"),
                            ("B", "Byte"),
                            ("W", "Word"),
                            ("DW", "Double_Word"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Valores",
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
                ("valor", models.FloatField(null=True)),
                ("fecha", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="scada.tags",
                    ),
                ),
            ],
        ),
    ]
