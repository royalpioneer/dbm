# Generated by Django 3.2.25 on 2024-04-30 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("db_monitor", "0018_auto_20231120_1654"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="dashboard",
            unique_together={("org_id", "org_name", "view", "cluster_type")},
        ),
    ]
