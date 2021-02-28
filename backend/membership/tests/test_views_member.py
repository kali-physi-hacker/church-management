import os
from datetime import datetime
from pathlib import Path

from django.core.files import File
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from membership.models import Member, Ministry, MaritalStatus
from common import error_messages, success_messages

BASE_DIR = Path(__file__).resolve().parent.parent

data = {
    "first_name": "Test-FN",
    "last_name": "Test-LN",
    "middle_name": "Test-MN",
    "email": "test@email.com",
    "age": 12,
    "date_of_birth": datetime.now().date(),
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


class DetailMemberViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.data = data.copy()

        self.data["ministry"] = Ministry.objects.create(name="Ushering", description="Ushering description")
        self.data["picture"] = File(open(os.path.join(BASE_DIR, "tests", "resources", "test_img.jpg"), "rb"))
        self.member = Member.objects.create(**self.data)
        self.data["id"] = self.member.pk
        self.data["ministry_id"] = self.data["ministry"].pk
        del self.data["ministry"]
        self.data["date_of_birth"] = str(self.data["date_of_birth"])

    def test_get_single_member(self):
        """
        Tests that user can get a single member
        :Return
        """
        response = self.client.get(reverse("membership:member_detail", args=(self.member.pk,)))
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 200)

        json_data = response.json()["member"]
        json_data["ministry_id"] = self.member.ministry.pk

        # Test picture path == /profile_photos/
        self.assertIn("profile_photos", json_data.get("picture").split("/"))
        self.assertEqual(
            json_data.get("picture").split("/")[-1].split("-")[0],
            self.data.get("picture").name.split("/")[-1].split(".")[0],
        )

        del json_data["picture"]

        for key in json_data:
            self.assertEqual(json_data.get(key), self.data.get(key))

    def test_get_single_member_returns_404_if_id_not_available(self):
        """
        Tests that single member returns 404 if id is not available
        :Return
        """
        response = self.client.get(reverse("membership:member_detail", args=(4,)))
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "member")

    def test_update_single_member_if_valid_id(self):
        """
        Tests that user can update a member details if specified id is valid
        :Return
        """
        update_data = {"first_name": "NewFN", "last_name": "NewLN"}
        response = self.client.put(reverse("membership:member_detail", args=(self.member.pk,)), data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.json()["message"], success_messages.UPDATE_SUCCESS % "member")

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
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "member")

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
        self.assertEqual(response.json()["message"], success_messages.DELETION_SUCCESS % "member")

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
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "member")


class ListMemberViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = data.copy()

        # self.data["ministry_id"] = Ministry.objects.create(name="Ushering", description="Ushering description").pk
        self.data["picture"] = File(open(os.path.join(BASE_DIR, "tests", "resources", "test_img.jpg"), "rb"))
        self.data["date_of_birth"] = str(self.data["date_of_birth"])

        self.data_1 = self.data.copy()
        self.data_2 = self.data.copy()
        self.data_1.update(
            {
                "first_name": "New FN 1",
                "picture": File(open(os.path.join(BASE_DIR, "tests", "resources", "test_img.jpg"), "rb")),
                "last_name": "New LN 1",
                "contact_1": "0000000000",
                "contact_2": "1111111111",
                "fathers_contact": "9459694059",
                "mothers_contact": "9111694059",
                "ministry": Ministry.objects.create(name="Data 1", description="Some Description"),
            }
        )
        self.data_2.update(
            {
                "picture": File(open(os.path.join(BASE_DIR, "tests", "resources", "test_img.jpg"), "rb")),
                "first_name": "New FN 2",
                "last_name": "New LN 2",
                "contact_1": "2222222222",
                "contact_2": "3333333333",
                "fathers_contact": "9400094059",
                "mothers_contact": "9400094119",
                "ministry": Ministry.objects.create(name="Data 2", description="Some Description 2"),
            }
        )

        Member.objects.create(**self.data_1)
        Member.objects.create(**self.data_2)

        self.data_1["ministry_id"] = self.data_1["ministry"].pk
        self.data_2["ministry_id"] = self.data_2["ministry"].pk
        self.data["ministry_id"] = Ministry.objects.create(name="Ushering", description="Ushering description").pk

    def test_can_create_member_if_valid_data(self):
        """
        Tests that user can create a member if submitted data values are valid
        :Returns:
        """
        response = self.client.post(reverse("membership:member_list"), data=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["success"])

        json_data = response.json()["member"]

        # Test picture path == /profile_photos/
        self.assertIn("profile_photos", json_data.get("picture").split("/"))
        self.assertEqual(
            json_data.get("picture").split("/")[-1].split("-")[0],
            self.data.get("picture").name.split("/")[-1].split(".")[0],
        )

        del json_data["picture"]

        self.data["id"] = json_data["id"]
        for key in json_data:
            self.assertEqual(json_data[key], self.data[key])

    def test_can_not_create_member_if_required_field_is_missing(self):
        """
        Tests that user cannot create a member if required field is missing on
        submitted data
        :Returns:
        """
        del self.data["first_name"]
        response = self.client.post(reverse("membership:member_list"), data=self.data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.json()["errors"]["first_name"][0], error_messages.FIELD_REQUIRED)

        # Test member is actually not created
        with self.assertRaises(Member.DoesNotExist):
            Member.objects.get(last_name=self.data["last_name"])

    def test_can_not_create_member_if_invalid_data(self):
        """
        Tests that user can not create a member if submitted data is invalid
        :Returns:
        """
        self.data["marital_status"] = "not accepted"
        response = self.client.post(reverse("membership:member_list"), data=self.data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json()["success"])
        self.assertEqual(
            response.json()["errors"]["marital_status"][0],
            error_messages.NOT_VALID_CHOICE % self.data["marital_status"],
        )

    def test_can_get_list_of_members(self):
        """
        Tests that user can a list of members with valid values
        :Returns:
        """
        response = self.client.get(reverse("membership:member_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["success"])

        member_1, member_2 = response.json()["members"][0:2]

        # Test for member 1 values

        # Test picture 1 path == /profile_photos/
        self.assertIn("profile_photos", member_1.get("picture").split("/"))
        self.assertEqual(
            member_1.get("picture").split("/")[-1].split("-")[0],
            self.data.get("picture").name.split("/")[-1].split(".")[0],
        )
        del member_1["picture"]

        del member_1["id"]
        for key in member_1:
            if member_1.get(key) != self.data_1.get(key):
                import pdb

                pdb.set_trace()
            self.assertEqual(member_1.get(key), self.data_1.get(key))

        # Test for member 2 values

        # Test picture 1 path == /profile_photos/
        self.assertIn("profile_photos", member_2.get("picture").split("/"))
        self.assertEqual(
            member_2.get("picture").split("/")[-1].split("-")[0],
            self.data.get("picture").name.split("/")[-1].split(".")[0],
        )
        del member_2["picture"]

        del member_2["id"]
        for key in member_2:
            self.assertEqual(member_2.get(key), self.data_2.get(key))


class UploadMemberViewTest(APITestCase):
    def setUp(self):

        self.client = APIClient()

        self.valid_file = File(open(os.path.join(BASE_DIR, "tests", "resources", "valid-members-file.csv"), "rb"))
        self.invalid_file = File(
            open(os.path.join(BASE_DIR, "tests", "resources", "invalid-members-file.csv"), "rb")
        )

    def test_uploads_correctly_if_valid_file(self):
        """
        Tests that file uploads correctly if correct file format and content
        """
        response = self.client.post(reverse("membership:member_upload"), data={"file": self.valid_file})
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["success"])
        self.assertEqual(Member.objects.all().count(), 5)
