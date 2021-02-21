import datetime
import pandas as pd

from rest_framework import serializers

from .models import Member
from .models import Ministry


def column_to_dict_map(columns, values):
    """
    Return a dictionary using the columns as keys and values as values for the keys
    :param columns:
    :param values:
    :return:
    """
    data = {}
    for index, col in enumerate(columns):
        data[col] = values[index]
    return data


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    ministry_id = serializers.PrimaryKeyRelatedField(
        source="ministry", queryset=Ministry.objects.all(), required=False
    )

    class Meta:
        model = Member
        exclude = ("is_active", "ministry")

    # def to_representation(self, instance):
    #     """
    #     Return the json for frontend
    #     """
    #     ministry = instance.ministry
    #     if ministry is not None:
    #         instance["ministry"] = ministry.name
    #
    #     return instance


class MemberUploadSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    file = serializers.FileField()

    def clean_none_values(self, member):
        """
        Clean nan values and make them None
        :param member:
        :return:
        """
        for key in member:
            if pd.isna(member[key]):
                member[key] = None

    def clean_member_date_of_birth(self, member):
        """
        Clean the date_of_birth field of the member
        :param member:
        :return:
        """
        try:
            day, month, year = member["date_of_birth"].split("/")
            member["date_of_birth"] = datetime.date(int(year), int(month), int(day))
        except:
            pass

    def clean_member_contacts(self, member):
        """
        Clean all phone numbers
        :param member:
        :return:
        """
        fields = ["contact_1", "contact_2", "mothers_contact", "fathers_contact"]
        for field in fields:
            if member[field]:
                if len(str(member[field])) == 9:
                    member[field] = f"0{member[field]}"
                member[field] = str(member[field])

    def clean_member_row(self, member):
        """
        Change all nan values to None values
        :param member:
        :return:
        """
        self.clean_none_values(member=member)
        self.clean_member_date_of_birth(member=member)
        self.clean_member_contacts(member=member)

    def validate_file(self, file):
        """
        Validate file and return a list of member serializers to be able to call .save() to save each
        one of them
        :param file:
        :return:
        """
        valid_serializers = []
        invalid_serializers = []

        fields = Member().excel_fields
        read_file = pd.read_csv(file)
        data_frame = pd.DataFrame(read_file, columns=fields)
        for member in data_frame.values:
            data = column_to_dict_map(columns=fields, values=member)
            self.clean_member_row(data)
            serializer = MemberSerializer(data=data)
            if not serializer.is_valid():
                invalid_serializers.append(serializer)

            valid_serializers.append(serializer)

        if len(invalid_serializers) > 0:
            raise serializers.ValidationError("Please check the content of the excel to make sure all values are correct")

        return valid_serializers

    def create(self, validated_data):
        """
        Saves the data in the db:
        :param validated_data:
        :return:
        """
        members = []
        data = validated_data["file"]
        for member_serializer in data:
            members.append(member_serializer.save())

        return members
