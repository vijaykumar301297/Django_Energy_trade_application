# Generated by Django 4.2.7 on 2024-01-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userManagement", "0004_alter_account_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
