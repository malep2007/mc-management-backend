from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny
from authentication.serializers import UserSerializer
from authentication.models import User

class UserList(
        ListModelMixin,
        CreateModelMixin,
        DestroyModelMixin,
        GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetail(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


# Create your views here.
