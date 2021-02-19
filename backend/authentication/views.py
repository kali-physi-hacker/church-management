from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserLoginSerializer


class LoginApiView(GenericViewSet):
    def login(self, request):
        """
        Authenticates a user and returns the user details
        :param request:
        :return
        """

        serializer = UserLoginSerializer(data=request.data)
        # import pdb; pdb.set_trace()
        response = {
            "success": True,
            "user": {
                "first_name": "TestFN",
                "last_name": "TestLN",
                "email": "test@email.com",
                "username": "test@email.com",
            },
        }
        return Response(data=response, status=status.HTTP_200_OK)
