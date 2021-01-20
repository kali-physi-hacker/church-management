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
        self.first_name = "Test-FN"
        self.last_name = "Test-LN"
        self.middle_name = "Test-MN"
        self.age = 12
        self.date_of_birth = "2001-03-03"
        self.ministry = Ministry.objects.create(name="Ushering", description="Ushering description")
        self.location = "Accra"
        self.contact_1 = "0123305678"
        self.contact_2 = "0123345678"
        self.occupation = "Teacher"
        self.is_student = True
        self.picture = File(os.path.join(BASE_DIR, "resources", "test_img.jpg"))
        self.mothers_contact = "0123456789"
        self.fathers_contact = "0122345678"
        self.marital_status = MaritalStatus.SINGLE
        self.children_no = 5

    def test_member_created_if_valid_fields(self):
        """
        Test that member is created when valid model fields are provided
        """
        member = Member.objects.create(
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            age=self.age,
            date_of_birth=self.date_of_birth,
            ministry=self.ministry,
            location=self.location,
            contact_1=self.contact_1,
            contact_2=self.contact_2,
            occupation=self.occupation,
            is_student=self.is_student,
            picture=self.picture,
            mothers_contact=self.mothers_contact,
            fathers_contact=self.fathers_contact,
            marital_status=self.marital_status,
            children_no=self.children_no,
        )

        expected_field_values = (
            self.first_name,
            self.middle_name,
            self.last_name,
            self.age,
            self.date_of_birth,
            self.ministry.pk,
            self.location,
            self.contact_1,
            self.contact_2,
            self.occupation,
            self.is_student,
            self.picture,
            self.mothers_contact,
            self.fathers_contact,
            self.marital_status,
            self.children_no,
            True,  # is_active field (default --> True)
        )

        actual_field_values = tuple(model_to_dict(member).values())[1:]
        for index, field_value in enumerate(actual_field_values):
            self.assertEqual(field_value, expected_field_values[index])

    def test_member_created_and_returns_valid_full_name(self):
        """
        Tests that member is created and returns valid full name
        """
        member = Member.objects.create(
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            age=self.age,
            date_of_birth=self.date_of_birth,
            ministry=self.ministry,
            location=self.location,
            contact_1=self.contact_1,
            contact_2=self.contact_2,
            occupation=self.occupation,
            is_student=self.is_student,
            picture=self.picture,
            mothers_contact=self.mothers_contact,
            fathers_contact=self.fathers_contact,
            marital_status=self.marital_status,
            children_no=self.children_no,
        )

        self.assertEqual(member.get_full_name(), f"{self.first_name} {self.middle_name} {self.last_name}")
