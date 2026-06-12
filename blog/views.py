from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,CommentUpdateSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostAPI(GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request):
        posts = self.get_queryset() # this will return me the query set
        serializer = self.get_serializer(
            posts,
            many = True
        ) # now serializer contains list of dictionaries

        return  Response(
            serializer.data
        )
        # this response converts python list of dictionaries into JSON String and revert back to frontend


    
    
    def post(self,request):

        serializer = self.get_serializer(
            data = request.data
        ) # this will only wrap my python dictionary object into serializable because request.data is already python dictionary

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save() # this will call .create under the hood

        return Response(
            {
                "msg" : "post created successfully"
            }
        )

        



class PostIdAPI(GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request,pk):
        post = self.get_object()
        serializer = self.get_serializer(
            post
        ) 
        return Response(serializer.data)


    def put(self,request,pk):
        post = self.get_object()
        serializer = self.get_serializer(
            post,
            data = request.data
        )

        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()

        return Response(
            {
                "msg" : "post updated successfully",
               
            } 
        )


        
        

    def patch(self,request,pk):
        post = self.get_object()
        serializer = self.get_serializer(
            post,
            data = request.data,
            partial = True
        )

        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()

        return Response({
            "msg" : "post updated successfully"
        })
       
    
    def delete(self,request,pk):
        post = self.get_object()
        post.delete()
        return Response(
            {
                 "msg" : "post deleted successfully"

            }
        )
        

  

class CommentAPI(GenericAPIView):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer


    def get(self, request):

     post_id = request.query_params.get("post")

     if post_id:

        comments = Comment.objects.filter(
            post=post_id
        )

     else:

        comments = self.get_queryset()

     serializer = self.get_serializer(
            comments,
            many=True
     ) 

     return Response(
        serializer.data
    )
        
        
     
    def post(self,request):
        serializer = self.get_serializer( 
            data = request.data
            )
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        
        return Response({
            "msg" : "comment posted successfully"
        })

    


class CommentIdAPI(GenericAPIView):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in ["PUT","PATCH"]:
            return CommentUpdateSerializer
        
        return CommentSerializer

    def get(self,request,pk):
        comment = self.get_object()

        serializer = self.get_serializer(
            comment
        ) 
        return Response(
            serializer.data
        )
        

    def put(self,request,pk):
       
        comment = self.get_object()
       
        serializer = self.get_serializer(
            comment,
            data = request.data
        )  
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        print(serializer.data["id"])
        return Response(
            {
                "msg" : "comment updated successfully"

            }
        )

       

    def patch(self,request,pk):
        comment = self.get_object()

        serializer = self.get_serializer(
            comment,
            data = request.data,
            partial = True
        ) 
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        return Response(
            {
                "msg" : "comment updated successfully"

            }
        )

        
    
    def delete(self,request,pk):
        comment = self.get_object()
        comment.delete()
        return  Response({
            "msg" : "comment deleted successfully"
        })
       

