from .views import PostAPI,PostIdAPI,CommentAPI,CommentIdAPI
from django.urls import path

urlpatterns = [
    path(
        "posts/",
        PostAPI.as_view()
    ),
    path(
        "posts/<int:pk>/",
        PostIdAPI.as_view()
    ),
    path(
        "comments/",
        CommentAPI.as_view()
    ),
    path(
        "comments/<int:pk>/",
        CommentIdAPI.as_view()
    ),

]