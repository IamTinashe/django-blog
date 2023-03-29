from rest_framework import serializers
from posts.models import BlogPost

class PostsSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields = '__all__'