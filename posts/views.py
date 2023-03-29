from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogPost
from .serializers import PostsSerializer
from rest_framework import status

@api_view(['GET'])
def getPosts(request):
  posts = BlogPost.objects.all()
  serializer = PostsSerializer(posts, many=True)
  return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def addPost(request):
  serializer = PostsSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
  else:
    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def editPost(request, id):
  post = BlogPost.objects.get(id=id)
  serializer = PostsSerializer(post, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
  else:
    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def viewPost(request, id):
  post = BlogPost.objects.get(id=id)
  serializer = PostsSerializer(post)
  return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deletePost(request, id):
  post = BlogPost.objects.get(id=id)
  post.delete()
  return Response({"status": "success", "message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)