# Generated by Django 2.2.3 on 2019-09-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meta_ae", "0005_auto_20190917_2032")]

    operations = [
        migrations.RemoveField(model_name="aeinitial", name="study_drug_relationship"),
        migrations.RemoveField(
            model_name="historicalaeinitial", name="study_drug_relationship"
        ),
        migrations.AddField(
            model_name="aeinitial",
            name="study_drug_relation",
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
                verbose_name="Relation to study drug:",
            ),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="study_drug_relation",
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
                verbose_name="Relation to study drug:",
            ),
        ),
    ]
