# Generated by Django 5.0.7 on 2024-08-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0146_grade_reminder_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="allow_drop_out",
            field=models.BooleanField(default=True, verbose_name="allow students to drop out"),
        ),
    ]
