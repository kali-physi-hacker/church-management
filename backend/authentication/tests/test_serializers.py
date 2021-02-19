from django.test import TestCase

from authentication.serializers import UserSignupSerializer

from common import error_messages


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            "first_name": "TestFN",
            "last_name": "TestLN",
            "email": "test@email.com",
            "password": "test@password",
            "confirm_password": "test@password"
        }

    def test_serializer_is_valid_if_required(self):
        """
        Tests that serializer.is_valid returns True if all required fields are passed
        :return
        """
        serializer = UserSignupSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_is_not_valid_if_missing_required_fields(self):
        """
        Tests that serializer.is_valid returns False if there is a missing required field
        :return
        """
        del self.user_data["confirm_password"]
        serializer = UserSignupSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["confirm_password"][0], error_messages.FIELD_REQUIRED)

    def test_serializer_is_not_valid_if_passwords_do_not_match(self):
        """
        Tests that serializer.is_valid returns False if password != confirm_password
        :return
        """
        self.user_data["confirm_password"] = "differentpassword"
        serializer = UserSignupSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_saves_user_if_valid(self):
        """
        Tests that serializer saves the user data in the db if serializer is valid
        :return
        """
        serializer = UserSignupSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        # Check that hashed password is the same
        self.assertTrue(user.check_password(self.user_data.get("password")))

        # Test that saved user is equal to user data provided
        del self.user_data["confirm_password"]
        del self.user_data["password"]
        for field in self.user_data:
            self.assertEqual(eval(f"user.{field}"), self.user_data.get(field))
