from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from membership.models import Member
from membership.serializers import MemberSerializer
from common import error_messages, success_messages


class MemberListView(APIView):
    def get(self, request, format=None):
        """
        Returns json response of the list of members
        :param request:
        :param format:
        :Returns:
        """
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(data={"success": True, "members": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Creates and returns a new member instance in the db
        :param request:
        :param format:
        """
        serializer = MemberSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        data = {"success": True, "message": success_messages.CREATION_SUCCESS % "member", "member": serializer.data}
        return Response(data=data, status=status.HTTP_201_CREATED)


class MemberDetailView(APIView):
    def get_member(self, pk):
        """
        Return a single member instance
        :param pk:
        :Returns:
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        """
        Return a json response of a single member instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        member = self.get_member(pk=pk)
        if member is None:
            return Response(
                data={"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "member"},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = {"success": True}
        serializer = MemberSerializer(member)
        data.update({"member": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        Updates and returns a single member instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        member = self.get_member(pk=pk)
        if member is None:
            return Response(
                data={"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "member"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MemberSerializer(member, data=request.data)
        if not serializer.is_valid():
            return Response(data={"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        data = {"success": True, "message": success_messages.UPDATE_SUCCESS % "member"}
        data.update({"member": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        """
        Deletes a single member instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        member = self.get_member(pk=pk)
        if member is None:
            return Response(
                data={"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "member"},
                status=status.HTTP_404_NOT_FOUND,
            )

        member.is_active = False
        member.save()

        return Response(
            data={"success": True, "message": success_messages.DELETION_SUCCESS % "member"},
            status=status.HTTP_202_ACCEPTED,
        )


class MemberExcelUpload(GenericViewSet):
    def upload(self, request, *args, **kwargs):
        """
        Add a list of members using an excel sheet
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = MemberUploadSerializer(data=request.data)
