# Generated by Django 5.1.1 on 2024-09-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0012_rename_added_date_cluster_records_addeddate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cluster_records",
            name="test_id",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cluster_records",
            name="timestamp",
            field=models.CharField(default="232", max_length=20),
            preserve_default=False,
        ),
    ]
