from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'title', 'author', 'created_date', 'text', 'public')