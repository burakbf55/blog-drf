from django.contrib.auth.decorators import login_required
from rest_framework import generics, mixins
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blog.api.paginations import PostPagination
from blog.api.serializers import PostDetailSerializer, PostSerializer, PostUpdateCreateSerializer
from blog.models import Comments, Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    lookup_field = "slug"
    search_fields = ("title", "description")

    def get_serializer_class(self):
        if self.action == "update":
            return PostUpdateCreateSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return super().get_serializer_class()


class CreatePostApiViews(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    # postu yazana custom permission eklenecek
    # permissions_classes = [IsAuthenticated]
    def perfom_create(self, serializer):
        serializer.save(author=self.request.user)


class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    search_fields = ["title", "description"]
    # filter_backends ekle
    # def get_queryset(self):
    #     return Post.objects.all()
    queryset = Post.objects.all()


class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
