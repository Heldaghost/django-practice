from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status, mixins, generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from phone_book.models import *
from phone_book.serializers import PhoneNoteSerializer, UserSerializer
from phone_book.permissions import *


@api_view(['GET'])
def api_home(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })

class NotesViewSet(viewsets.ModelViewSet):
    queryset = PhoneNote.objects.all()
    serializer_class = PhoneNoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class NoteList(generics.ListCreateAPIView):
#     queryset = PhoneNote.objects.all()
#     serializer_class = PhoneNoteSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PhoneNote.objects.all()
#     serializer_class = PhoneNoteSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
