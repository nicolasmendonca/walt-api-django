from rest_framework import generics, permissions
from user.authentication import BearerTokenAuthentication
from user.serializers import CustomUserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    permission_classes = []
    serializer_class = CustomUserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    permission_classes = []
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    authentication_classes = (BearerTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

