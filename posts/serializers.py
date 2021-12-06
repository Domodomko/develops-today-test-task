from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "link", "creation_date", "upvotes_ammount", "author")
        read_only_fields = ("creation_date", "upvotes_ammount", "author")
