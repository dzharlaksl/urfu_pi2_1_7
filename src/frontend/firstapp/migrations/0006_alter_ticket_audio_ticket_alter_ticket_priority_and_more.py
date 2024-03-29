# Generated by Django 5.0.3 on 2024-03-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0005_alter_employee_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="audio_ticket",
            field=models.FileField(upload_to="media"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="priority",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="text_ticket",
            field=models.CharField(max_length=5000),
        ),
    ]
