from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,CommentUpdateSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostAPI(APIView):

    def get(self,request):
        posts = Post.objects.all() # this will return me the query set
        serializer = PostSerializer(
            posts,
            many = True
        ) # now serializer contains list of dictionaries

        return  Response(
            serializer.data
        )
        # this response converts python list of dictionaries into JSON String and revert back to frontend


    
    
    def post(self,request):

        serializer = PostSerializer(
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

        



class PostIdAPI(APIView):

    def get(self,request,id):
        post = get_object_or_404(Post,id = id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def put(self,request,id):
        post = get_object_or_404(Post,id = id)
        serializer = PostSerializer(
            post,
            data = request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(
            {
                "msg" : "post updated successfully",
               
            } 
        )


        
        

    def patch(self,request,id):
        post = get_object_or_404(Post,id = id)
        serializer = PostSerializer(
            post,
            data = request.data,
            partial = True
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response({
            "msg" : "post updated successfully"
        })
       
    
    def delete(self,request,id):
        post = get_object_or_404(Post,id = id)
        post.delete()
        return Response(
            {
                 "msg" : "task deleted successfully"

            }
        )
        

  

class CommentAPI(APIView):
    # def get(self,request):
    #     comments = Comment.objects.all()
    #     serializer = CommentSerializer(
    #         comments,
    #         many = True
    #     )
    #     return Response(
    #         serializer.data,
    #     )

    # def get(self,request):
    #     postId = request.query_params.get("post")
    #     post = get_object_or_404(Post,id = postId)
    #     comments = Comment.objects.filter(post = post)
    #     serializer = CommentSerializer(
    #         comments,
    #         many = True
    #     )
    #     return Response(
    #         serializer.data,
    #     )
  

    def get(self, request):

     post_id = request.query_params.get("post")

     if post_id:

        comments = Comment.objects.filter(
            post=post_id
        )

     else:

        comments = Comment.objects.all()

     serializer = CommentSerializer(
        comments,
        many=True
    )

     return Response(
        serializer.data
    )
        
        
     
    def post(self,request):
        serializer = CommentSerializer(
            data = request.data
            )
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        
        return Response({
            "msg" : "comment posted successfully"
        })

        



class CommentIdAPI(APIView):

    def get(self,request,id):
        comment = get_object_or_404(Comment,id = id)
        serializer = CommentSerializer(comment)
        return Response(
            serializer.data
        )
        

    def put(self,request,id):
        comment = get_object_or_404(Comment,id = id)
        print(comment.id)
        serializer = CommentUpdateSerializer(
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

       

    def patch(self,request,id):
        comment = get_object_or_404(Comment,id = id)
        serializer = CommentUpdateSerializer(
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

        
    
    def delete(self,request,id):
        comment = get_object_or_404(Comment,id = id)
        comment.delete()
        return  Response({
            "msg" : "comment deleted successfully"
        })
       

