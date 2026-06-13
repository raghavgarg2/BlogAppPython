# from .views import PostAPI,PostIdAPI,CommentAPI,CommentIdAPI
from django.urls import path

from .views import PostViewSet,CommentViewSet


urlpatterns = [
    path(
        "posts/",
        PostViewSet.as_view({
            "get" : "list",
            "post" : "create"

        })
    ),
    path(
        "posts/<int:pk>/",
        PostViewSet.as_view({
            "get" : "retrieve",
            "put" : "update",
            "patch" : "partial_update",
            "delete" : "destroy"
        })
    ),
    path(
        "comments/",
        CommentViewSet.as_view({
            "get" : "list",
            "post" : "create"
        })
    ),
     path(
        "comments/<int:pk>/",
        CommentViewSet.as_view({
            "get" : "retrieve",
            "put" : "update",
            "patch" : "partial_update",
            "delete" : "destroy"
        })
    )

]


# urlpatterns = [
#     path(
#         "posts/",
#         PostAPI.as_view()
#     ),
#     path(
#         "posts/<int:pk>/",
#         PostIdAPI.as_view()
#     ),
#     path(
#         "comments/",
#         CommentAPI.as_view()
#     ),
#     path(
#         "comments/<int:pk>/",
#         CommentIdAPI.as_view()
#     ),

# ]