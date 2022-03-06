from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets

from .serializers import UserSerializer
from users import serializers

# Example of viewset to the as the others views
# This can replace other views but it will lost with readability


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Generic views for example
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
