# Generated by Django 2.2.3 on 2019-09-13 18:50

from django.db import migrations
import edc_action_item.managers


class Migration(migrations.Migration):

    dependencies = [("meta_ae", "0002_auto_20190913_1524")]

    operations = [
        migrations.AlterModelManagers(
            name="aeinitial",
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierManager()),
            ],
        )
    ]