from rest_framework import serializer

from .models import BlogPost

class BlogPostSerializer(Serializer.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
        ]
