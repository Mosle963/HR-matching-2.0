# Generated by Django 5.1.1 on 2024-09-21 07:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email_address"
                    ),
                ),
                ("is_employee", models.BooleanField(default=False)),
                ("is_company", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("name", models.CharField(help_text="Company Name", max_length=100)),
                ("city", models.CharField(help_text="Company City", max_length=100)),
                ("phone", models.CharField(help_text="Company Phone", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "firstname",
                    models.CharField(
                        help_text="Employee First Name",
                        max_length=100,
                        verbose_name="First Name",
                    ),
                ),
                (
                    "lastname",
                    models.CharField(
                        help_text="Employee Last Name",
                        max_length=100,
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "dateOfBirth",
                    models.DateField(
                        help_text="Employee Date of Birth", verbose_name="Date Of Birth"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("MALE", "MALE"), ("FEMALE", "FEMALE")], max_length=8
                    ),
                ),
                ("city", models.CharField(help_text="Employee City", max_length=50)),
                ("phone", models.CharField(help_text="Employee Phone", max_length=20)),
                ("education", models.TextField(blank=True, max_length=1000, null=True)),
                (
                    "experience",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                ("awards", models.TextField(blank=True, max_length=1000, null=True)),
                ("hobbies", models.TextField(blank=True, max_length=1000, null=True)),
                ("skills", models.TextField(max_length=1000)),
                (
                    "references",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                ("other", models.TextField(blank=True, max_length=1000, null=True)),
                ("cluster", models.IntegerField(blank=True, null=True)),
                ("clusterable_text", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
