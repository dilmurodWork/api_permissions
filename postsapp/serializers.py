from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PostModel


class PostsSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = PostModel
        fields = '__all__'
