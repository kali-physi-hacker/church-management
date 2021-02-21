import pandas as pd

from rest_framework import serializers

from .models import Member
from .models import Ministry


class MinistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ministry
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    ministry_id = serializers.PrimaryKeyRelatedField(
        source="ministry",
        queryset=Ministry.objects.all(),
        required=False
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

    def validate_file(self, file):
        """
        Validate file and return a list of member serializers to be able to call .save() to save each
        one of them
        :param file:
        :return:
        """
        fields = [field.name for field in Member._meta.get_field()]
        read_file = pd.read_excel(file)
        data_frame = pd.DataFrame(read_file, columns=fields)
        import pdb

        pdb.set_trace()
