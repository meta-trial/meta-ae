# Generated by Django 2.2.3 on 2019-09-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meta_ae", "0004_auto_20190916_2019")]

    operations = [
        migrations.AddField(
            model_name="aeinitial",
            name="study_drug_relationship",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Relationship to study drug:",
            ),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="study_drug_relationship",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Relationship to study drug:",
            ),
        ),
    ]
