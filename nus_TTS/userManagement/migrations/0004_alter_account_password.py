# Generated by Django 4.2.7 on 2024-01-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userManagement", "0003_rename_account_status_account_account_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="password",
            field=models.CharField(max_length=400, null=True),
        ),
    ]
