from rest_framework import serializers
from books.models import Art, Chapter, Tag
from user_center.models import ArtsUser
from message.models import Comment


class ArtsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsUser
        fields = [
            'id',
            'username',
            'password',
            'email',
            'isActive',
            'createtime',
            'flag',

        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            't_name',
            't_info',
            't_createtime',
            't_flag',
        ]


class ArtSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source="operator.username")

    class Meta:
        model = Art
        fields = [
            'id',
            'a_title',
            'a_info',
            'a_content',
            'a_img',
            'a_createtime',
            'a_tag',
            'a_price',
            'a_flag',
            'operator',
        ]


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'art',
            'title',
            'content',
            'create_time',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'title',
            'text',
            'created_time',
            'art',
            'flag',
        ]
