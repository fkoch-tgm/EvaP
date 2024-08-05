# Generated by Django 5.1.1 on 2024-10-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0147_evaluation_allow_drop_out"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionnaire",
            name="type",
            field=models.IntegerField(
                choices=[
                    (10, "Top questionnaire"),
                    (20, "Contributor questionnaire"),
                    (30, "Bottom questionnaire"),
                    (40, "Dropout questionnaire"),
                ],
                default=10,
                verbose_name="type",
            ),
        ),
    ]
