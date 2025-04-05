from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from mytodo.models import Todo
from mytodo.serializers import TodoSerializer, RegisterSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Account is inactive'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})



class ListCreateTodoView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.roles.lower() == 'user' or user.is_superuser:
            return Todo.objects.filter(is_public=True) | Todo.objects.filter(is_flagged=True) | Todo.objects.filter(owner=user)
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyTodoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_update(self, serializer):
        user = self.request.user
        todo = self.get_object()
        data = self.request.data

        if user.roles.lower() == 'moderator':
            serializer.save()
        elif todo.owner == user:
            if todo.is_flagged and data.get('is_public') == True:
                raise serializers.ValidationError("This todo is flagged and cannot be made public again.")
            if 'is_flagged' in data:
                raise serializers.ValidationError("You cannot modify 'is_flagged'")
            serializer.save()
        else:
            raise PermissionDenied("You don't have permission to update this.")


# Public Todos List (Anyone can view)
class PublicTodoListView(generics.ListAPIView): 
    queryset = Todo.objects.filter(is_public=True)
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]


    
    
    

