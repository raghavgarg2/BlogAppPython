from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,CommentUpdateSerializer
from rest_framework.response import Response
from rest_framework.mixins import (ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin)
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class PostAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostIdAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

   
        

  

# class CommentAPI(CreateModelMixin,ListModelMixin,GenericAPIView):

#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get(self, request):

#      post_id = request.query_params.get("post")

#      if post_id:
#         comments = Comment.objects.filter(
#             post=post_id
#         )
#      else:
#         comments = self.get_queryset()
#         serializer = self.get_serializer(
#             comments,
#             many=True
#      ) 

#      return Response(
#         serializer.data
#     )
        
        
#     def post(self,request):
#         self.create(request)
        
class CommentAPI(ListCreateAPIView):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_queryset(self):

        post_id = self.request.query_params.get("post")

        if post_id:
            return Comment.objects.filter(
                post=post_id
            )
        print(self.queryset)
        # return self.queryset
        # return Comment.objects.all()
        # return self.queryset.all()
        return super().get_queryset()

   

class CommentIdAPI(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in ["PUT","PATCH"]:
            return CommentUpdateSerializer
        
        return CommentSerializer

   
 

class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()

    serializer_class = PostSerializer




class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_queryset(self):

        post_id = self.request.query_params.get("post")

        if post_id:
            return Comment.objects.filter(
                post=post_id
            )

        return super().get_queryset()

    def get_serializer_class(self):

        if self.action in [
            "update",
            "partial_update"
        ]:
            return CommentUpdateSerializer

        return CommentSerializer