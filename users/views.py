from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStaff, IsActive, IsSuperUser
from users.serializers import UserSerializer, UserCreateSerializer, UserTokenObtainPairSerializer, UserUpdateSerializer, \
    UserRetrieveSerializer

from users.models import User


class UserListAPIView(ListAPIView):
    """ List для модели User """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaff]


class UserCreateAPIView(CreateAPIView):
    """ Create для модели User """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """ Retrieve для модели User """

    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperUser]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserUpdateAPIView(UpdateAPIView):
    """ Update для модели User """

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserDestroyAPIView(DestroyAPIView):
    """ Destroy для модели User """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
