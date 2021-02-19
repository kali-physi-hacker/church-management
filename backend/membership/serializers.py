import pandas as pd

from rest_framework import serializers

from .models import Member
from .models import Ministry


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    ministry = serializers.SerializerMethodField()

    class Meta:
        model = Member
        exclude = ("is_active",)

    def get_ministry(self, instance):
        """
        Return ministry name
        :param instance:
        :return:
        """
        ministry = instance.ministry
        if ministry is not None:
            return ministry.name

    def validate_ministry(self, data):
        """
        Accept ministry id and set instance ministry to be ministry instance
        :param data:
        :return:
        """
        try:
            data["ministry"] = Ministry.objects.get(pk=data["ministry"])
        except Ministry.DoesNotExist:
            raise serializers.ValidationError({"ministry": "Does not exist"})

    def run_validation(self, data):
        """
        Clean the data and make all empty strings None
        :param data:
        :return
        """

        cleaned_data = data
        for field in data:
            if data[field] == "":
                cleaned_data[field] = None

        self.validate_ministry(cleaned_data)
        return cleaned_data


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
        import pdb; pdb.set_trace()
