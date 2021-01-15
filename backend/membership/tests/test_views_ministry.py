from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from membership import success_messages, error_messages
from membership.models import Ministry


class DetailMinistryViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.ministry_data = {
            "name": "Ushering",
            "description": "Some ushering description"
        }

        self.ministry = Ministry.objects.create(
            name=self.ministry_data.get("name"),
            description=self.ministry_data.get("description"),
        )

    def test_get_single_ministry(self):
        """
        Tests that user can get a single ministry instance
        :Returns:
        """
        response = self.client.get(reverse("membership:ministry_detail", args=(self.ministry.pk,)))
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ministry"].get("name"), self.ministry.name)
        self.assertEqual(response.json()["ministry"].get("description"), self.ministry.description)
        self.assertEqual(response.json()["ministry"].get("id"), self.ministry.pk)

    def test_get_single_ministry_returns_404_if_id_not_available(self):
        """
        Tests that 404 is returned if user tries to get ministry with unavailable id
        :Returns:
        """
        response = self.client.get(reverse("membership:ministry_detail", args=(2,)))
        self.assertFalse(response.json()["success"])
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Ministry")

    def test_update_single_ministry_if_valid_id(self):
        """
        Tests that user can update a single ministry if ministry exists
        :Returns:
        """
        name_update = "Name Updated"
        description_update = "Ushering Description Updated"
        response = self.client.put(
            reverse("membership:ministry_detail", args=(self.ministry.pk,), ),
            {"name": name_update, "description": description_update}
        )
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], success_messages.UPDATE_SUCCESS % "Ministry")
        self.assertEqual(response.json()["ministry"].get("name"), name_update)
        self.assertEqual(response.json()["ministry"].get("description"), description_update)

        # Test db instance
        ministry = Ministry.objects.get(pk=self.ministry.pk)
        self.assertEqual(ministry.name, name_update)
        self.assertEqual(ministry.description, description_update)

    def test_update_single_ministry_returns_404_if_id_not_found(self):
        """
        Tests that 404 is returned if ministry id does not exist
        :Returns:
        """
        name_update = "Name Updated"
        description_update = "Ushering Description Updated"
        response = self.client.put(
            reverse("membership:ministry_detail", args=(2,), ),
            {"name": name_update, "description": description_update}
        )

        self.assertFalse(response.json()["success"])
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Ministry")

        # Test that no new ministry instance is created
        with self.assertRaises(Ministry.DoesNotExist):
            Ministry.objects.get(name=name_update)

    def test_delete_single_ministry_if_valid_id(self):
        """
        Tests that user can delete a single ministry instance provided id is valid
        :Returns:
        """
        response = self.client.delete(reverse("membership:ministry_detail", args=(1,)))
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["message"], success_messages.DELETION_SUCCESS % "Ministry")

        # Test that it is not available in the db
        with self.assertRaises(Ministry.DoesNotExist):
            Ministry.objects.get(pk=self.ministry.pk)

        self.assertEqual(0, len(Ministry.objects.all()))

    def test_delete_single_ministry_returns_404_if_invalid_id(self):
        """
        Tests that 404 is returned if id does not exist
        :Returns:
        """
        response = self.client.delete(reverse("membership:ministry_detail", args=(2,)))

        self.assertFalse(response.json()["success"])
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], error_messages.OBJECT_DOES_NOT_EXIST % "Ministry")


class MinistryViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.ministry_data = {
            "name": "Ushering",
            "description": "Some ushering description"
        }

    def test_can_add_ministry_if_valid_post_request_body(self):
        """
        Tests that user can add member if valid post request body
        :Returns:
        """
        pass
        # response = self.client.post(reverse("membership:ministry_detail"), self.ministry_data)
        # self.assertTrue(response.json()["success"])
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.json()["message"], success_messages.CREATION_SUCCESS)
        # self.assertEqual(response.json()["ministry"].get("name"), self.ministry_data.get("name"))
        # self.assertEqual(response.json()["ministry"].get("description"), self.ministry_data.get("description"))

    def test_can_not_add_member_if_name_field_not_present(self):
        """
        Tests that user can not add member if name field is not present in post
        request body
        :Returns:
        """
        pass

    def test_can_not_add_member_if_name_already_exist(self):
        """
        Tests that user can not add member if name value already exist
        :Returns:
        """
        pass
