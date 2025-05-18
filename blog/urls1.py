from django.urls import path

from . import views

urlpatterns = [
    # path("", views.starting_page, name="starting"),
    path("", views.StartingPageView.as_view(), name="starting"),
    path("posts", views.PostsView.as_view(), name="posts"),
    # path("posts/<slug:slug1>", views.PostDetail.as_view(), name="posts_detail")  # /posts/my-first-post called slug. and slug is checker for this as str check for string.
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="posts_detail")  # /posts/my-first-post called slug. and slug is checker for this as str check for string.
    
]
