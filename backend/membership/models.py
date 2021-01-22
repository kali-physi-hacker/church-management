import os
import random
from uuid import uuid4 as _

from django.db import models
from django.core.validators import RegexValidator


phone_number_validator = RegexValidator(
    regex=r"^\+?1?\d{10,13}$", message="Phone number be entered in the format: +233123456789"
)


def get_filename_ext(file_path):
    """
    Return a tuple containing the filename and extension
    :param file_path:
    """
    base = os.path.basename(file_path)
    name, ext = os.path.splitext(base)
    return name, ext


RANDOM_UPPER_LIMIT = 9999999


def upload_path(instance, filename):
    """
    Return a random name for saving file
    :param instance:
    :param filename:
    """
    name, ext = get_filename_ext(filename)
    random_file_name = f"{random.randint(1, RANDOM_UPPER_LIMIT)}-{_()}{ext}"
    return f"profile_photos/{name}-{random_file_name}"


class Ministry(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        String representation of ministry
        """
        return self.name


class ActiveMemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class DeletedMemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class MaritalStatus:
    SINGLE = "SINGLE"
    MARRIED = "MARRIED"


class Member(models.Model):

    MARITAL_STATUS_CHOICES = ((MaritalStatus.MARRIED, "Married"), (MaritalStatus.SINGLE, "Single"))

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, null=True, blank=True)
    contact_1 = models.CharField(
        validators=[phone_number_validator], max_length=13, unique=True, blank=True, null=True
    )
    contact_2 = models.CharField(
        validators=[phone_number_validator], max_length=13, unique=True, blank=True, null=True
    )
    occupation = models.CharField(max_length=120, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=upload_path, max_length=250)
    mothers_contact = models.CharField(
        validators=[phone_number_validator], max_length=13, unique=True, blank=True, null=True
    )
    fathers_contact = models.CharField(
        validators=[phone_number_validator], max_length=13, unique=True, blank=True, null=True
    )
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=7, default=MaritalStatus.SINGLE)
    children_no = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = ActiveMemberManager()
    deleted = DeletedMemberManager()

    def get_full_name(self):
        """
        Return the fullname of the person
        """
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        """
        Return member string representation
        """
        return f"{self.get_full_name()} - {self.location}"
