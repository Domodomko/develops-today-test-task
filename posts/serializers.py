from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "link", "creation_date", "upvotes_ammount", "author")
        read_only_fields = ("creation_date", "upvotes_ammount", "author")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "creation_date", "author", "post")
        read_only_fields = ("creation_date", "author", "post")


class PostWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "link",
            "creation_date",
            "upvotes_ammount",
            "author",
            "comments",
        )
