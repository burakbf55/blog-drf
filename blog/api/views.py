from rest_framework import generics
from blog.models import Post,Comments
from blog.api.serializers import PostSerializer, PostUpdateCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from blog.api.paginations import PostPagination
from django.contrib.auth.decorators import login_required

class CreatePostApiViews(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    #postu yazana custom permission eklenecek
    # permissions_classes = [IsAuthenticated]
    def perfom_crate(self,serializer):
        serializer.save(author = self.request.user)
    

class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    search_fields = ['title','description']
    #filter_backends ekle
    def get_queryset(self):
        return Post.objects.all()



class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    