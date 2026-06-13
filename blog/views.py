from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,CommentUpdateSerializer
from rest_framework.response import Response
from rest_framework.mixins import (ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin)


class PostAPI(ListModelMixin,CreateModelMixin,GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request):
        return self.list(request)


    def post(self,request):
        return self.create(request)

        



class PostIdAPI(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request,pk):
        return self.retrieve(request)


    def put(self,request,pk):
        return self.update(request)
        
        

    def patch(self,request,pk):
       return self.partial_update(request)
       
    
    def delete(self,request,pk):
        return self.destroy(request)
        

  

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
        
class CommentAPI(
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView
):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_queryset(self):

        post_id = self.request.query_params.get("post")

        if post_id:

            return Comment.objects.filter(
                post=post_id
            )

        return self.queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CommentIdAPI(UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericAPIView):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in ["PUT","PATCH"]:
            return CommentUpdateSerializer
        
        return CommentSerializer

    def get(self,request,pk):
        return self.retrieve(request)
        

    def put(self,request,pk):
        return self.update(request)

       

    def patch(self,request,pk):
       return self.partial_update(request)

        
    
    def delete(self,request,pk):
        return self.destroy(request)

