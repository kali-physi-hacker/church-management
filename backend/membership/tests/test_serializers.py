import os
from pathlib import Path
from datetime import datetime

from django.test import TestCase
from django.core.files import File

from membership.serializers import MinistrySerializer, MemberSerializer, MemberUploadSerializer
from membership.models import Ministry, MaritalStatus
from common.error_messages import FIELD_REQUIRED, FIELD_UNIQUE

BASE_DIR = os.path.join(Path(__file__).resolve().parent.parent, "tests", "resources")


class MinistrySerializerTest(TestCase):
    def setUp(self):
        self.name = "Ushering"
        self.description = "Some description for ushers"

    def test_ministry_is_valid_if_required_fields_present(self):
        """
        Tests that ministry serializer is_valid is True and creates ministry instance
        when all required fields are correctly provided
        :Returns:
        """
        serializer = MinistrySerializer(data={"name": self.name, "description": self.description})

        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(validated_data.get("name"), self.name)
        self.assertEqual(validated_data.get("description"), self.description)

    def test_ministry_is_invalid_if_name_field_not_present(self):
        """
        Tests that ministry serializer is_valid is False and does not create ministry instance
        when name field is not present
        :Returns:
        """
        serializer = MinistrySerializer(data={"description": self.description})

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.validated_data, {})
        self.assertEqual(serializer.errors.get("name")[0], FIELD_REQUIRED)

    def test_ministry_is_invalid_if_same_name(self):
        """
        Tests that ministry serializer is_valid is False and does not create ministry instance
        when the ministry name already exists
        :Returns:
        """
        serializer = MinistrySerializer(data={"name": self.name, "description": self.description})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        serializer = MinistrySerializer(data={"name": self.name, "description": self.description})

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.validated_data, {})
        self.assertEqual(serializer.errors.get("name")[0], FIELD_UNIQUE % "ministry")

    def test_ministry_serializer_saves_if_valid_data(self):
        """
        Tests that ministry serializer saves if valid data
        :Return
        """
        serializer = MinistrySerializer(data={"name": self.name, "description": self.description})

        self.assertTrue(serializer.is_valid())
        ministry = serializer.save()

        self.assertEqual(ministry.name, self.name)
        self.assertEqual(ministry.description, self.description)


class MemberSerializerTest(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Test-FN",
            "last_name": "Test-LN",
            "middle_name": "Test-MN",
            "email": "test@email.com",
            "age": 12,
            "date_of_birth": datetime.now().date(),
            "picture": File(open(os.path.join(BASE_DIR, "test_img.jpg"), "rb")),
            "ministry_id": Ministry.objects.create(name="Ushering", description="Ushering description").pk,
            "location": "Test location",
            "contact_1": "0123302678",
            "contact_2": "0123345698",
            "occupation": "Teacher",
            "is_student": True,
            "mothers_contact": "0123456789",
            "fathers_contact": "0122345678",
            "marital_status": MaritalStatus.SINGLE,
            "children_no": 5,
        }

    def test_member_is_valid_if_all_required_fields(self):
        """
        Tests that member is_valid is true if all required fields are present
        and all values valid
        :Returns:
        """
        serializer = MemberSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        serializer.validated_data["ministry_id"] = 1
        for key in serializer.validated_data.keys():
            if key == "ministry":
                self.assertEqual(serializer.validated_data.get(key).pk, self.data.get("ministry_id"))
            else:
                self.assertEqual(serializer.validated_data.get(key), self.data.get(key))

    def test_member_is_invalid_if_some_required_fields_missing(self):
        """
        Tests that member is_valid is false if some required or all required fields
        are not present
        :Returns:
        """
        del self.data["first_name"]
        serializer = MemberSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.validated_data), 0)

    def test_member_serializer_saves_if_valid_data(self):
        """
        Tests that member serializer saves if valid data
        :Returns:
        """
        serializer = MemberSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        serializer.save()


class UploadMemberSerializerTest(TestCase):
    def setUp(self):
        self.valid_file = File(open(os.path.join(BASE_DIR, "valid-members-file.csv"), 'rb'))
        self.invalid_file = File(open(os.path.join(BASE_DIR, "invalid-members-file.csv"), 'rb'))

    def test_is_valid_returns_true_if_excel_file_content_is_valid(self):
        """
        Tests that is_valid returns True if data content of the excel sheet is valid
        :return:
        """
        serializer = MemberUploadSerializer(data={"file": self.valid_file})
        self.assertTrue(serializer.is_valid())

    def test_valid_data_saves_correctly(self):
        """
        Tests that serializer saves the data correctly if valid
        :return:
        """
        serializer = MemberUploadSerializer(data={"file": self.valid_file})
        self.assertTrue(serializer.is_valid())
        members = serializer.save()
        # More tests to come here to test that data is created with the exact values

    def test_is_valid_returns_false_if_excel_file_content_is_not_valid(self):
        """
        Tests that is_valid returns False if data content of the excel sheet is not valid
        :return:
        """
        serializer = MemberUploadSerializer(data={"file": self.invalid_file})
        self.assertFalse(serializer.is_valid())

    def test_invalid_data_not_saves(self):
        """
        Tests that serializer can not save if is not valid
        :return:
        """
        serializer = MemberUploadSerializer(data={"file": self.invalid_file})
        self.assertFalse(serializer.is_valid())

        # Is valid is not true so cannot save
        with self.assertRaises(AssertionError):
            serializer.save()