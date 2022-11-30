# Generated by Django 4.1.3 on 2022-11-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asignaturas",
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
                ("codigo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.CharField(max_length=200)),
            ],
        ),
    ]