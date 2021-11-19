from django.urls import path
from blog.api.views import (
    CreatePostApiViews,
    ListPostAPIView,
    DetailPostAPIView
)

#router kullan

app_name = "blog"
urlpatterns = [
    path("",ListPostAPIView.as_view(),name="list_post"),
    path("create/",CreatePostApiViews.as_view(),name="create_post"),
    path("<str:slug>/",DetailPostAPIView.as_view(),name="detail_post")
    ]

