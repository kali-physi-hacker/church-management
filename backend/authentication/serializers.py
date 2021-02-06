from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=120)
    last_name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=150)
    confirm_password = serializers.CharField(max_length=150)

    def validate_email(self, email):
        """
        Raise serializer ValidationError if email already exist
        :param email:
        :return
        """
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError("User with that email already exist")
        except User.DoesNotExist:
            return email

    def validate_password(self, password):
        """
        Raise serializer ValidationError if password != confirm_password
        :param password:
        :return
        """
        confirm_password = self.initial_data.get("confirm_password")  # Will refactor this
        if password != confirm_password:
            raise serializers.ValidationError("Password mismatch")
        return password

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        del validated_data["confirm_password"]

        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user
