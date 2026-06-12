from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


