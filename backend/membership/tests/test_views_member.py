import os
from datetime import datetime
from pathlib import Path

from django.core.files import File
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from membership.models import Member, Ministry, MaritalStatus
from membership import error_messages, success_messages


BASE_DIR = Path(__file__).resolve().parent.parent


class DetailMemberViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.data = {
            "first_name": "Test-FN",
            "last_name": "Test-LN",
            "middle_name": "Test-MN",
            "age": 12,
            "date_of_birth": datetime.now().date(),
            "picture": File(open(os.path.join(BASE_DIR, "tests", "resources", "test_img.jpg"), "rb")),
            "ministry": Ministry.objects.create(name="Ushering", description="Ushering description"),
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
        self.member = Member.objects.create(**self.data)
        self.data["id"] = self.member.pk
        self.data["ministry"] = self.data["ministry"].pk
        self.data["date_of_birth"] = str(self.data["date_of_birth"])

    def test_get_single_member(self):
        """
        Tests that user can get a single member
        :Return
        """
        response = self.client.get(reverse("membership:member_detail", args=(self.member.pk,)))
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 200)

        data = response.json()["member"]
        data["ministry"] = self.member.pk

        # Test picture path == /profile_photos/
        self.assertEqual(data.get("picture").split("/")[1], "profile_photos")
        self.assertEqual(
            data.get("picture").split("/")[2].split("-")[0],
            self.data.get("picture").name.split("/")[-1].split(".")[0],
        )

        del data["picture"]

        for key in data:
            self.assertEqual(data.get(key), self.data.get(key))

    def test_get_single_member_returns_404_if_id_not_available(self):
        """
        Tests that single member returns 404 if id is not available
        :Return
        """
        response = self.client.get(reverse("membership:member_detail", args=(4,)))
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Member")

    def test_update_single_member_if_valid_id(self):
        """
        Tests that user can update a member details if specified id is valid
        :Return
        """
        update_data = {"first_name": "NewFN", "last_name": "NewLN"}
        response = self.client.put(reverse("membership:member_detail", args=(self.member.pk,)), data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.json()["message"], success_messages.UPDATE_SUCCESS % "Member")

        # Test updated fields
        self.assertEqual(response.json()["member"].get("first_name"), update_data.get("first_name"))
        self.assertEqual(response.json()["member"].get("last_name"), update_data.get("last_name"))

    def test_update_single_member_returns_404_if_id_not_available(self):
        """
        Tests that 404 is returned if specified id is not available
        :Return
        """
        response = self.client.put(
            reverse("membership:member_detail", args=(2,)), data={"first_name": "NewFn", "last_name": "NewFn"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Member")

        # Test that no new ministry instance is created
        with self.assertRaises(Member.DoesNotExist):
            Member.objects.get(first_name="NewFn")

    def test_delete_single_member_if_valid_id(self):
        """
        Tests that user can delete a single member instance provided id is valid
        :Return
        """
        response = self.client.delete(reverse("membership:member_detail", args=(self.member.pk,)))
        self.assertEqual(response.status_code, 202)
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.json()["message"], success_messages.DELETION_SUCCESS % "Member")

        # Test that member cannot be accessed using the default ModelManager
        with self.assertRaises(Member.DoesNotExist):
            Member.objects.get(pk=self.member.pk)

        # Test that member is actually not deleted but marked inactive
        member = Member.deleted.get(pk=self.member.pk)
        self.assertFalse(member.is_active)

    def test_delete_single_member_returns_404_if_invalid_id(self):
        """
        Tests that 404 is returned if id does not exist
        :Return
        """
        response = self.client.delete(reverse("membership:member_detail", args=(2,)))
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Member")
