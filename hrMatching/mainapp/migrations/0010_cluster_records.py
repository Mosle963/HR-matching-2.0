# Generated by Django 5.1.1 on 2024-09-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0009_employee_cluster_jobpost_cluster_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cluster_records",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("added_date", models.DateField()),
                ("silhouette_score", models.FloatField()),
                ("calinski_harabasz_score", models.FloatField()),
                ("number_of_clusters", models.IntegerField()),
                ("total_records", models.IntegerField()),
                ("word2vec_vector_size", models.IntegerField()),
                ("word2vec_window_size", models.IntegerField()),
                ("word2vec_word_min_count_percentage", models.FloatField()),
                ("from_date", models.DateField()),
                ("applied", models.BooleanField()),
                ("inertia", models.FloatField()),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
