# Generated by Django 5.1.3 on 2025-01-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0147_unusable_password_default"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="dropout_count",
            field=models.IntegerField(default=0, verbose_name="dropout count"),
        ),
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