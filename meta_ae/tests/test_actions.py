from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, tag
from edc_action_item.models import ActionItem
from edc_constants.constants import CLOSED, NEW
from edc_facility.import_holidays import import_holidays
from edc_randomization.management.commands import import_randomization_list
from model_mommy import mommy
from edc_adverse_event.constants import (
    AE_FOLLOWUP_ACTION,
    AE_TMG_ACTION,
    DEATH_REPORT_ACTION,
    DEATH_REPORT_TMG_ACTION,
)
from edc_reportable.constants import GRADE4, GRADE5
from meta_screening.tests.meta_test_case_mixin import MetaTestCaseMixin


class TestActions(MetaTestCaseMixin, TestCase):
    @classmethod
    def setUpClass(cls):
        import_holidays()
        import_randomization_list
        return super(TestActions, cls).setUpClass()

    def test_ae_initial_creates_action(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        ae_initial = mommy.make_recipe(
            "meta_ae.aeinitial", subject_identifier=subject_consent.subject_identifier
        )

        try:
            action_item = ActionItem.objects.get(
                action_identifier=ae_initial.action_identifier
            )
        except ObjectDoesNotExist:
            self.fail("ObjectDoesNotExist unexpectedly raised.")
        else:
            self.assertEqual(action_item.status, CLOSED)
            self.assertEqual(
                action_item.subject_identifier, subject_consent.subject_identifier
            )

    def test_ae_initial_creates_ae_followup_action(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        ae_initial = mommy.make_recipe(
            "meta_ae.aeinitial", subject_identifier=subject_consent.subject_identifier
        )

        action_item = ActionItem.objects.get(
            action_identifier=ae_initial.action_identifier
        )
        try:
            action_item = ActionItem.objects.get(
                parent_action_item=action_item,
                action_type__name=AE_FOLLOWUP_ACTION,
                subject_identifier=subject_consent.subject_identifier,
            )
        except ObjectDoesNotExist:
            self.fail("ObjectDoesNotExist unexpectedly raised.")
        else:
            self.assertEqual(action_item.status, NEW)

    def test_ae_initial_G4_creates_ae_tmg_action(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        mommy.make_recipe(
            "meta_ae.aeinitial",
            subject_identifier=subject_consent.subject_identifier,
            ae_grade=GRADE4,
        )

        try:
            ActionItem.objects.get(
                action_type__name=AE_TMG_ACTION,
                subject_identifier=subject_consent.subject_identifier,
            )
        except ObjectDoesNotExist:
            self.fail("ObjectDoesNotExist unexpectedly raised.")

    def test_ae_initial_G5_creates_death_report_action(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        mommy.make_recipe(
            "meta_ae.aeinitial",
            subject_identifier=subject_consent.subject_identifier,
            ae_grade=GRADE5,
        )
        try:
            ActionItem.objects.get(
                action_type__name=DEATH_REPORT_ACTION,
                subject_identifier=subject_consent.subject_identifier,
            )
        except ObjectDoesNotExist:
            self.fail("ObjectDoesNotExist unexpectedly raised.")

        self.assertRaises(
            ObjectDoesNotExist,
            ActionItem.objects.get,
            action_type__name=DEATH_REPORT_TMG_ACTION,
            subject_identifier=subject_consent.subject_identifier,
        )

    def test_death_report_create_death_report_tmg_action(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        mommy.make_recipe(
            "meta_ae.aeinitial",
            subject_identifier=subject_consent.subject_identifier,
            ae_grade=GRADE5,
        )
        action_item = ActionItem.objects.get(
            action_type__name=DEATH_REPORT_ACTION,
            subject_identifier=subject_consent.subject_identifier,
        )

        mommy.make_recipe(
            "meta_ae.deathreport",
            subject_identifier=subject_consent.subject_identifier,
            action_identifier=action_item.action_identifier,
        )

        action_item.refresh_from_db()
        self.assertEqual(action_item.status, CLOSED)

        try:
            action_item = ActionItem.objects.get(
                action_type__name=DEATH_REPORT_TMG_ACTION,
                subject_identifier=subject_consent.subject_identifier,
            )
        except ObjectDoesNotExist:
            self.fail("ObjectDoesNotExist unexpectedly raised.")
        else:
            self.assertEqual(action_item.status, NEW)
