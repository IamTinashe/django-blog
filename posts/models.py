from django.db import models
from users.models import User

class BlogPost(models.Model):
  author_id = models.BigIntegerField(null=True)
  title = models.CharField(max_length=200)
  content = models.CharField(max_length=5000)
  # image = models.ImageField(upload_to='blog_images')
  tags = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title