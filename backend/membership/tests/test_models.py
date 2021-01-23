import os
from pathlib import Path

from django.test import TestCase
from django.db import IntegrityError
from django.core.files import File
from django.forms.models import model_to_dict

from membership.models import Ministry, Member, MaritalStatus

BASE_DIR = Path(__file__).resolve().parent.parent


class MinistryModelTest(TestCase):
    def setUp(self):
        self.name = "Ushering"
        self.description = "Cleaning of church, maintaining order and guiding members"

    def test_ministry_created_if_valid_fields(self):
        """
        Tests that ministry instance is created when valid fields are provided
        """
        ministry = Ministry.objects.create(name=self.name, description=self.description)
        self.assertEqual(ministry.name, self.name)
        self.assertEqual(ministry.description, self.description)

        # Assert query length is 1
        self.assertEqual(len(Ministry.objects.all()), 1)

    def test_ministry_errors_if_same_name(self):
        """
        Tests that ministry creation errors if name field is empty
        """
        Ministry.objects.create(name=self.name, description=self.description)

        with self.assertRaises(IntegrityError):
            Ministry.objects.create(name=self.name, description=self.description)


class MemberModelTest(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Test-FN",
            "last_name": "Test-LN",
            "middle_name": "Test-MN",
            "email_address": "test@email.com",
            "age": 12,
            "date_of_birth": "2001-03-03",
            "ministry": Ministry.objects.create(name="Ushering", description="Ushering description"),
            "location": "Accra",
            "contact_1": "0123305678",
            "contact_2": "0123345678",
            "occupation": "Teacher",
            "is_student": True,
            "picture": File(os.path.join(BASE_DIR, "resources", "test_img.jpg")),
            "mothers_contact": "0123456789",
            "fathers_contact": "0122345678",
            "marital_status": MaritalStatus.SINGLE,
            "children_no": 5
        }

    def test_member_created_if_valid_fields(self):
        """
        Test that member is created when valid model fields are provided
        """
        member = Member.objects.create(**self.data)

        member_dict = model_to_dict(member)
        self.data["ministry"] = self.data["ministry"].pk
        for key in self.data.keys():
            self.assertEqual(member_dict.get(key), self.data.get(key))

        self.assertTrue(member.is_active)

    def test_member_created_and_returns_valid_full_name(self):
        """
        Tests that member is created and returns valid full name
        """
        member = Member.objects.create(**self.data)

        self.assertEqual(member.get_full_name(), f"{self.data['first_name']} {self.data['middle_name']} {self.data['last_name']}")
