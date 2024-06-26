# Generated by Django 5.0.6 on 2024-06-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "authentication",
            "0004_studentslist_application_status_studentslist_city_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="studentslist",
            name="comments",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="studentslist",
            name="gender",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Other", "Other"),
                    ("Not Selected", "Not Selected"),
                ],
                default="Not Selected",
                max_length=12,
            ),
        ),
    ]
