# Generated by Django 5.1.7 on 2025-03-31 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_placementcompany_alter_placementprofile_cgpa"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="placementprofile",
            name="percentage_10th",
            field=models.DecimalField(decimal_places=2, default=None, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="placementprofile",
            name="percentage_12th",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="PlacementApplication",
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
                ("resume", models.FileField(upload_to="resume/")),
                ("other_details", models.JSONField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
