# Generated by Django 5.1.1 on 2024-09-29 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0011_alter_cluster_records_added_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cluster_records",
            old_name="added_date",
            new_name="addedDate",
        ),
        migrations.RenameField(
            model_name="job_post",
            old_name="added_date",
            new_name="addedDate",
        ),
    ]
