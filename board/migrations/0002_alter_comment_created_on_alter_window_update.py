# Generated by Django 4.1.3 on 2022-11-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="window",
            name="update",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]