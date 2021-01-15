from rest_framework import serializers

from .models import Member
from .models import Ministry


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
