from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient


User = get_user_model()


class LoginTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user_data = {
            "first_name": "TestFN",
            "last_name": "TestLN",
            "email": "test@email.com",
            "username": "test@email.com",
            "password": "password",
        }

        self.user = User.objects.create(**self.user_data)
        self.user.set_password(self.user_data.get("password"))

    def test_login_returns_200_and_user_id_if_valid_credentials(self):
        """
        Tests that login endpoint returns 200 status code and user id if valid credentials
        are provided
        :return
        """
        response = self.client.post(reverse("authentication:login"), data=self.user_data)
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.status_code, 200)

        del self.user_data["password"]

        for field in self.user_data:
            self.assertEqual(response.json().get("user").get(field), eval(f"self.user.{field}"))

        """
        response = {
            success: True,
            user: {
                first_name: "", last_name: "", email: "", id: ""
            }
        }
        """
