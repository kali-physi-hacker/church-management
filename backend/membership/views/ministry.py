from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from membership.models import Ministry
from membership.serializers import MinistrySerializer
from membership import error_messages, success_messages


class MinistryListView(APIView):
    def get(self, request, format=None):
        """
        Returns json response of the list of ministries
        :param request:
        :param format:
        :Returns:
        """
        pass

    def post(self, request, format=None):
        """
        Creates and returns a new ministry instance in the db
        :param request:
        :param format:
        """
        pass


class MinistryDetailView(APIView):
    def get_ministry(self, pk):
        """
        Return a single ministry instance
        :param pk:
        :Returns:
        """
        try:
            return Ministry.objects.get(pk=pk)
        except Ministry.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        """
        Return a json response of a single ministry instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        ministry = self.get_ministry(pk=pk)
        if ministry is None:
            return Response({"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "Ministry"},
                            status=status.HTTP_404_NOT_FOUND)

        data = {"success": True}
        serializer = MinistrySerializer(ministry)
        data.update({"ministry": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        Updates and returns a single ministry instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        ministry = self.get_ministry(pk=pk)
        if ministry is None:
            return Response(data={"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "Ministry"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = MinistrySerializer(ministry, data=request.data)

        if not serializer.is_valid():
            return Response(data={"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        data = {"success": True, "message": success_messages.UPDATE_SUCCESS % "Ministry", }
        data.update({"ministry": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        """
        Deletes a single ministry instance
        :param request:
        :param pk:
        :param format:
        :Returns:
        """
        ministry = self.get_ministry(pk=pk)
        if ministry is None:
            return Response(data={"success": False, "error": error_messages.OBJECT_DOES_NOT_EXIST % "Ministry"}, status=status.HTTP_404_NOT_FOUND)

        ministry.delete()

        return Response(data={"success": True, "message": success_messages.DELETION_SUCCESS % "Ministry"}, status=status.HTTP_202_ACCEPTED)
