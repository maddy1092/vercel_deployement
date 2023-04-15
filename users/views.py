from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

# Create your views here.
User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UserSignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
            "message": "User created successfully.",
            "user": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
