#lookup_field araştır
from rest_framework import permissions
from rest_framework.views import APIView
from accounts.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from accounts.api.permissions import IsOwner

User = get_user_model()
class UserCreateAPIView(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsAuthenticated]

#query seti filtreliyerek ownerı getir
class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsAuthenticatedOrReadOnly,IsOwner]


class UpdatePasswordAPIView(APIView):
    def put(self,request,*args,**kwargs):
        pass

