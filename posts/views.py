from rest_framework import generics, viewsets

from users import serializers

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

# Example of viewset to the as the others views
# This can replace other views but it will lost with readability


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Generic views for example
# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated, )
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
