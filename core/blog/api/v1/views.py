from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    mixins,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializers(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class PostList(
    # ListAPIView,
    ListCreateAPIView
    # GenericAPIView,
    # mixins.ListModelMixin,
    #   mixins.CreateModelMixin
):
    """"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def get(self, request):
    #     """"""
    #     posts = Post.objects.filter(status=True)
    #     serializer = PostSerializers(posts, many=True)
    #     return Response(serializer.data)
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def post(self, request):
    #     """"""
    #     serializer = PostSerializers(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


# @api_view(["GET", "PUT", "DELETE"])
# def postDetail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializers(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializers(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(
#             {"message": "Post deleted successfully"}, status=status.HTTP_200_OK
#         )
# try:
#     post = Post.objects.get(pk=id)
#     serializer = PostSerializers(post)
#     return Response(serializer.data)
# except Post.DoesNotExist:
#     return Response(
#         {"detail": "post does not exist"}, status=status.HTTP_404_NOT_FOUND
#     )
class PostDetail(
    # GenericAPIView,
    # mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    # def get(self, requset, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)

    # def put(self, requset, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     serializer = self.serializer_class(post, data=self.requset.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     post.delete()
    #     return Response(
    #         {"message": "Post deleted successfully"}, status=status.HTTP_200_OK
    #     )
