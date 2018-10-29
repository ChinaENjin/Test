from rest_framework import viewsets
from rest_framework import permissions

from books.models import Art, Tag, Chapter
from user_center.models import ArtsUser
from drf_apis.permissions import IsOwnerOrReadOnly
from message.models import Comment
from drf_apis import serializers


class ArtsUserViewSet(viewsets.ModelViewSet):
    queryset = ArtsUser.objects.all()
    serializer_class = serializers.ArtsUserSerializer

    permission_classes = (IsOwnerOrReadOnly,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    permission_classes = (IsOwnerOrReadOnly,)


class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = serializers.ArtSerializer

    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
