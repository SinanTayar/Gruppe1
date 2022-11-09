# Generated by Django 4.1.2 on 2022-11-09 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answers",
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
                ("answer_text", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Questions",
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
                ("field_type", models.CharField(max_length=255)),
                ("text", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
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
                ("type", models.CharField(max_length=255)),
                (
                    "answer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.answers"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Forms",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answers",
            name="question_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.questions"
            ),
        ),
        migrations.AddField(
            model_name="answers",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.user"
            ),
        ),
    ]
