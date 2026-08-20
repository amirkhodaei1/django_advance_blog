from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from ...models import Category, Post
from .paginations import DefaultPagination
from .permissions import isOwnerOrReadOnly
from .serializers import CategorySerializer, PostSerializer

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request)
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
    serializer_class = PostSerializer
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
# class PostDetail(
# GenericAPIView,
# mixins.RetrieveModelMixin,
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin,
# RetrieveUpdateDestroyAPIView
# ):
# permission_classes = [IsAuthenticatedOrReadOnly]
# serializer_class = PostSerializer
# queryset = Post.objects.filter(status=True)
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


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({"detail": "ok"})

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data)

    # def create(self, request):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
